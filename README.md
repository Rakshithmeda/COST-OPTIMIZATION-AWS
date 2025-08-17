# COST-OPTIMIZATION-AWS
Introduction
Managing AWS costs efficiently requires monitoring and removing unused resources. This project addresses cost savings by detecting Elastic Block Store (EBS) snapshots that are no longer associated with any active EC2 instance. By eliminating these stale snapshots, unnecessary storage charges are avoided.

Components
AWS Lambda
AWS Lambda is a serverless compute service that executes code in response to events. It automatically manages the infrastructure required to run the function. In this project, the Lambda function is responsible for scanning all snapshots, identifying the ones that are no longer needed, and deleting them.
Amazon EC2
Amazon Elastic Compute Cloud (EC2) offers resizable compute capacity in the AWS cloud. The state of EC2 instances is used to check whether their related snapshots are still required.
How It Works
1. Snapshot Identification (Data Collection)
The Lambda function retrieves every EBS snapshot created under the account. For example, if snapshots were taken from EC2 instances that no longer exist, they are marked for review.
2. Snapshot Validation
Each snapshot is cross-checked against currently active EC2 instances. If the original volume of a snapshot is not attached to a running or stopped EC2 instance, that snapshot is classified as stale.
3. Snapshot Deletion
Once stale snapshots are identified, the Lambda function removes them. This cleanup process can be triggered on a schedule to ensure regular cost optimization without manual intervention.
Summary
The Lambda function collects all snapshots in the account, validates them against existing EC2 instances, and removes the ones that are unused. This automated approach helps continuously optimize AWS storage expenses by eliminating stale snapshots.
