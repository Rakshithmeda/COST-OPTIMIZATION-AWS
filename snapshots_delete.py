import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    try:
        instance_id = event['detail']['instance-id']
        print(f"Terminated EC2 instance: {instance_id}")
    except KeyError:
        print("Instance ID not found in the event")
        return

    # Get all snapshots owned by this account
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    
    # Try to find volumes that were attached (optional)
    volumes = []
    try:
        instance_data = ec2.describe_instances(InstanceIds=[instance_id])
        for reservation in instance_data['Reservations']:
            for instance in reservation['Instances']:
                for bd in instance.get('BlockDeviceMappings', []):
                    volume_id = bd['Ebs']['VolumeId']
                    volumes.append(volume_id)
    except Exception as e:
        print("Instance info not found (possibly terminated), skipping volume check.")
    
    # Search for snapshots with matching instance or volume info in their descriptions
    for snap in snapshots:
        snapshot_id = snap['SnapshotId']
        desc = snap.get('Description', '')
        if instance_id in desc or any(vol_id in desc for vol_id in volumes):
            try:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot: {snapshot_id} linked to terminated instance {instance_id}")
            except Exception as e:
                print(f"Error deleting snapshot {snapshot_id}: {e}")
