import requests
from requests.adapters import HTTPAdapter
from streamlit.connections import ExperimentalBaseConnection

class Bored_APIConnection(ExperimentalBaseConnection[requests.Session]):

    def __init__(self, connection_name: str):

        self._connect()

        self.url = "https://www.boredapi.com/api/activity"

        super().__init__(connection_name)

    def _connect(self) -> requests.Session:
        """Connects to the Session

        :returns: requests.Session
        """
        session = requests.Session()
        session.mount("https://", HTTPAdapter(max_retries=5))
        return session

    def query_any_activity(self):

        response = requests.get(self.url).json()
        return response['activity']


    def query_specific_activity(self, accessibility, prices, types, participants):        

        activities = []

        for _ in types:
            payload = {
                "type": _,
                "participants": participants,
                "minprice": prices[0],
                "maxprice": prices[1],
                "minaccessibility": accessibility[0],
                "maxaccessibility" : accessibility[1]
            }
            response = requests.get(self.url, data=payload)
            activities.append(response.json()['activity'])
        return activities
