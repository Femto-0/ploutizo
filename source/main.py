import processImage as pi
import query_apollo as qa
import query_ollama as qo
import cleanEnrichedData as ced
model = "llama3.2"


def main():
    # write the name of your image here without the extension. For example: for "imageA.jpg", just write "imageA"
    image = 'IMG_5293'
    imageInfo = pi.extract_text_from_image('images/'+image+'.PNG')
    ollama_response = qo.query_ollama(imageInfo, model)
    # get raw data from ollama
    raw_data = qa.query_apollo(ollama_response)
    # clean the raw data and filter out the info that we want.
    # As of now, the filter data contains:
    # ['first_name','last_name','linkedin_url','organization_name','title','email','last_job','last_job_title']
    clean_data = ced.extract_relevant_data(raw_data)
    # save the clean data in a json and xlsx file
    ced.cleanData(clean_data, image)


if __name__ == "__main__":
    main()
