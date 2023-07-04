Take a copy of code and create a new file

change only in this block, dont copy entire thing, just replace "Append `ticket_data` instead of `extracted_ticket_data`" that is last line , I have added !! mark for that line

for ticket_data in open_tickets:
    ticket_id = ticket_data["Id"]
    ticket_url = f"{url}/api/v1/data/serviceTickets/{ticket_id}"
    ticket_response = requests.get(ticket_url, headers=headers, params=params, verify=False)
    ticket_response_data = ticket_response.json()

    extracted_ticket_data = {
        "Id": ticket_data["Id"],
        "Status": ticket_data["Status"],
        "deviceUUID": ticket_response_data.get("deviceUUID")
    }

    ticket_data.update(extracted_ticket_data)
    !!extracted_data.append(ticket_data)  # Append `ticket_data` instead of `extracted_ticket_data!!


