import ec2ops

def ec2stop(event, context):

    print("Receive event: {}".format(event))
    ec2ops.stop_running_instance()
    return {
        "message": "Success"
    }

def ec2start(event, context):

    print("Receive event: {}".format(event))
    ec2ops.start_stopped_instance()
    return {
        "message": "Success"
    }

def setasginstancesize(event, context):

    print("Receive event: {}".format(event))
    asgops.update_autoscalinggroup(event)
    return {
        "message": "Success"
    }
