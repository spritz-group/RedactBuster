import os
import json
import requests

def case_json_download(id, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

    if not os.path.exists(f'{dir}/{id}.json'.format(dir, id)):
        url = 'https://echr-opendata.eu/api/v1/cases/{0}'.format(id)
        headers = {'accept': 'application/json'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open('{0}/{1}.json'.format(dir, id), 'w') as file:
                json.dump(response.json(), file, indent=2)
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

def case_pdf_download(id, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

    if not os.path.exists(f'{dir}/{id}.pdf'):
        url = 'https://hudoc.echr.coe.int/app/conversion/docx/pdf?library=ECHR&id={0}&filename={1}.pdf'.format(id, id)
        headers = {'accept': 'application/json'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open('{0}/{1}.pdf'.format(dir, id), 'wb') as file:
                file.write(response.content)
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

##########################################################
######################### main ###########################
##########################################################
def main():
    for e in ['train', 'test', 'dev']:
        if not os.path.exists(f"{e}/pdf/"):
            os.makedirs(f"{e}/pdf/")
        if not os.path.exists(f"{e}/json/"):
            os.makedirs(f"{e}/json/")

        annotation = f'echr_{e}.json'
        with open(annotation, 'r') as file:
            data = json.load(file)

        print(f'\n{e.upper()}')
        # data = data[:5]
        for i, item in enumerate(data):
            doc_id = item.get('doc_id', None)
            if doc_id is not None:
                case_json_download(doc_id, f"./{e}/json/")
                case_pdf_download(doc_id, f"./{e}/pdf/")
                print('({0}/{1} | {2}%) {3}'.format(i+1, len(data), round(((i+1)*100)/len(data), 1), doc_id))


if __name__ == "__main__":
    main()