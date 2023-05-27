from .train import Model
import requests
from bs4 import BeautifulSoup

class Chatbot(object):
    def __init__(self):
        self.model = Model()
        self.model.load_model('models.pkl')
        self.data = None

    def chat(self, msg):
        msg = msg.lower()
        return self.response(msg)
        

    def response(self, sentence):
        predicted_words = self.model.predict(sentence)
        if predicted_words :
            return " ".join(predicted_words)
        else:
            return self.query(sentence)

    def query(self, text):
        user_query = text
        URL = "https://www.google.co.in/search?q=" + user_query
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57"
        }
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        bebe = str(soup)
        if 'class="LGOjhe"' in bebe:
            sult = soup.find(class_="LGOjhe").find(class_="hgKElc").get_text()
            return sult
        if 'class="Y2IQFc"' in bebe:
            sult = soup.find(id="tw-target-text").get_text()
            return sult
        elif 'class="vk_bk dDoNo FzvWSb"' in bebe:
            sult = soup.find(class_="vk_bk dDoNo FzvWSb").get_text()
            return sult
        elif 'class="Z0LcW"' in bebe:
            sult = soup.find(class_="Z0LcW").get_text()
            return sult
        elif 'class="pclqee"' in bebe:
            sult = soup.find(class_="pclqee").get_text()
            return sult + " VNĐ"
        elif 'class="LGOjhe"' in bebe:
            sult = soup.find(class_="LGOjhe").find(class_="hgKElc").get_text()
            return sult
        elif 'class="FzvWSb"' in bebe:
            sult = soup.find(class_="FzvWSb").get_text()
            return sult
        elif 'class="z7BZJb XSNERd"' in bebe:
            sult = soup.find(class_="qv3Wpe").get_text()
            return sult
        elif 'class="dDoNo ikb4Bb gsrt"' in bebe:
            sult = soup.find(class_="dDoNo ikb4Bb gsrt").get_text()
            return sult
        elif 'class="ayRjaf"' in bebe:
            sult = soup.find(class_="zCubwf").get_text()
            return sult
        elif 'class="dDoNo vrBOv vk_bk"' in bebe:
            sult = soup.find(class_="dDoNo vrBOv vk_bk").get_text()
            return sult
        elif 'class="hgKElc"' in bebe:
            sult = soup.find(class_="hgKElc").get_text()
            return sult
        elif 'class="UQt4rd"' in bebe:
            nhietdo = " Nhiệt độ: " + soup.find(class_="q8U8x").get_text() + "°C "
            doam = " Độ ẩm: " + soup.find(id="wob_hm").get_text()
            mua = " Khả năng có mưa: " + soup.find(id="wob_pp").get_text()
            gdp = soup.find(class_="wob_tci")
            wheather = gdp["alt"]
            nam = wheather + nhietdo + mua + doam
            return nam
        elif 'class="gsrt vk_bk FzvWSb YwPhnf"' in bebe:
            sult = soup.find(class_="gsrt vk_bk FzvWSb YwPhnf").get_text()
            return sult
        else:
            if len(text) > 0:
                return "Xin lỗi tôi không hiểu bạn nói gì. Bạn có thể nói rõ hơn được không"