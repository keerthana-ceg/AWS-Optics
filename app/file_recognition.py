import boto3

def recognize_pdf(file):
    """
    Performs text detection on the given pdf
    Param: file - file to analyze
    """
    client=boto3.client('textract', region_name='us-west-2')

    # convert pdf to image
    pages = convert_pdf_to_img(file)

    # concat to make single image
    file_image = concat_images(pages)

    #convert image to byte
    byte_img = convert_image_to_byte(file_image)

    # call textract service
    try:
        response = client.detect_document_text(Document={'Bytes': byte_img})
        blocks=response['Blocks']
        overall_text = []
        for block in blocks:
            if  block['BlockType'] == 'LINE':
                overall_text.append(block['Text'])
        text = overall_text
        return{
                "text": {
                        "pages": len(pages),
                        "text": text
                    }
            }
