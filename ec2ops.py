""" This module provide function to start and stop EC2 instance """
import boto3

EC2 = boto3.resource('ec2')

def fetch_instance(filters):
    ''' Fetch EC2 instance by specify filters
    '''
    instances = EC2.instances.filter(Filters=filters)

    instances_id = []
    for instance in instances:
        instances_id.append(instance.id)

    return instances_id

def start_stopped_instance():
    ''' Start EC2 instance
    '''
    filters = [{'Name':'tag:AutoStart', 'Values':['Yes', 'YES', 'true']},
               {'Name': 'instance-state-name', 'Values': ['stopped']}]
    print("Filters: {}".format(filters))

    instances_id = fetch_instance(filters)
    print("StoppedInstance: {}".format(instances_id))

    if instances_id:
        EC2.instances.filter(InstanceIds=instances_id).start()

    return

def stop_running_instance():
    ''' Stop running EC2 instance
    '''
    filters = [{'Name':'tag:AutoStop', 'Values':['Yes', 'YES', 'true']},
               {'Name': 'instance-state-name', 'Values': ['running']}]
    print("Filters: {}".format(filters))

    instances_id = fetch_instance(filters)
    print("RunningInstance: {}".format(instances_id))

    if instances_id:
        EC2.instances.filter(InstanceIds=instances_id).stop()

    return
