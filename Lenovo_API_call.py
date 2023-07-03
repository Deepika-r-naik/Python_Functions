#### This is to fetch the ticket Id from the API and then iterate through each Id to fetch each ticket details####


def fetch_data():
    url = "https://test"
    headers = {'Authorization': 'Basic ...'}
    params = {}

    try:
        response = requests.get(url, headers=headers, params=params, verify=False)
        response.raise_for_status()

        if response.status_code == 200:
            response_data = response.json()
            open_tickets = [
                {
                    "Id": ticket["id"], 
                    "Status": ticket["state"],
                    "PMRType": ticket["PMRType"],
                    "PmrUID": ticket["PmrUID"],
                    "componentName": ticket["componentName"],
                    "ticketType": ticket["ticketType"],
                    "createDate": ticket["createDate"]
                }
                for ticket in response_data.get("results", [])
                if ticket.get("state") != "Closed"
            ]
            
            extracted_data = []
            
            for ticket_data in open_tickets:
                ticket_id = ticket_data["Id"]
                ticket_url = f"{url}/{ticket_id}"
                ticket_response = requests.get(ticket_url, headers=headers, params=params, verify=False)
                ticket_response_data = ticket_response.json()

                extracted_ticket_data = {
                    "Id": ticket_data["Id"],
                    "Status": ticket_data["Status"],
                    "deviceUUID": ticket_response_data.get("deviceUUID")
                }

                ticket_data.update(extracted_ticket_data)
                
                extracted_data.append(extracted_ticket_data)

            for ticket_data in open_tickets:
                ticket_data["Status"] = ticket_data.pop("Status")

            return open_tickets, extracted_data

        else:
            print("Error: Unable to fetch data from the API")
            return [], []
    except Exception as e:
        print(f"Error: {e}")

def main():
    open_tickets, extracted_data = fetch_data()
    
    json_output = json.dumps(open_tickets, indent=4)
    print("Open Tickets:")
    print(json_output)
    
    extracted_data_output = json.dumps(extracted_data, indent=4)
    print("Extracted Data:")
    print(extracted_data_output)

main()
