import processImage as pi
import query_apollo as qa
import query_ollama as qo
import cleanEnrichedData as ced
model = "llama3.2"


def main():
    imageInfo = pi.extract_text_from_image('images/annotatedTestPic.PNG')
    ollama_response = qo.query_ollama(imageInfo, model)
    data = qa.query_apollo(ollama_response)
    ced.cleanData(data)


if __name__ == "__main__":
    main()
