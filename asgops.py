""" This module provide funciton to update auto scaling group """
import boto3

AUTO_SCALING = boto3.client('autoscaling')

def update_autoscalinggroup(param):
    '''Updates the configuration for the specified Auto Scaling group.
    '''

    response = AUTO_SCALING.update_auto_scaling_group(
        AutoScalingGroupName=param['AsgGroupName'],
        MinSize=param['MinSize'],
        DesiredCapacity=param['DesiredCapacity'],
    )
    print(response)
    return
