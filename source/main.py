import processImage as pi
import query_apollo as qa
import query_ollama as qo
import cleanEnrichedData as ced
model = "llama3.2"


def main():
    # write the name of your image here without the extension. For example: linkedInImage, image fromGoogle, etc.
    image = 'IMG_5293'
    imageInfo = pi.extract_text_from_image('images/'+image+'.PNG')
    ollama_response = qo.query_ollama(imageInfo, model)
    data = qa.query_apollo(ollama_response)
    ced.cleanData(data, image)


if __name__ == "__main__":
    main()
