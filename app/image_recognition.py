import boto3

def aws_optics_summary(photo):
    '''
        Method to get the complete analysis of the given Image
        Param: photo - image to analyze
    '''
    return "hi"

def detect_labels(photo):
    '''
        Method to detect the labels in the photo.
        Param: photo - path to the photo
    '''
    # Initialize boto3 client
    client=boto3.client('rekognition', region_name='us-west-2')

    # read file
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    # read response
    for label in response['Labels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))

def detect_text(photo):
    '''
    Method to detect txt in the given image
    Param: photo - path of the image
    '''
    # Initialize boto3 client
    client=boto3.client('rekognition')

    # Read image file
    with open(photo, 'rb') as image:
        response=client.detect_text(Image={'Bytes': image.read()})

    # Response from AWS Rekognition
    textDetections=response['TextDetections']
    for text in textDetections:
        if text['Type'] == 'LINE':
            print(text['DetectedText'] + ' : ' + str("{:.2f}".format(text['Confidence']) + "%"))

    return len(textDetections)

def moderate_image(photo):
    '''
    Method to detection the modration labels in the given image
    Param: photo - path to the image
    '''
    # Initiate boto3 client
    client=boto3.client('rekognition')

    # Read the image file
    with open(photo, 'rb') as image:
        response = client.detect_moderation_labels(Image={'Bytes': image.read()})

    # Response from AWS Rekognition
    print('Detected labels for ' + photo)
    for label in response['ModerationLabels']:
        print (label['Name'] + ' : ' + str(label['Confidence']))
        print (label['ParentName'])
    return len(response['ModerationLabels'])
