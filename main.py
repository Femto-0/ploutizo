import processImage as pi
import query_apollo as qa
import query_ollama as qo

model = "llama3.2"


def main():
    imageInfo = pi.extract_text_from_image('images/IMG_5293.PNG')
    ollama_response = qo.query_ollama(imageInfo, model)
    qa.query_apollo(ollama_response)


if __name__ == "__main__":
    main()
