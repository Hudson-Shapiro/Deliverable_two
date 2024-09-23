import csv

# Change .csv file name here !!
csv_file1 = "meets/56th_Holly-Duane_Raffin_Festival_of_Races_Mens_5000_Meters_D1_Boys_24.csv"
csv_file2 = "meets/Bret_Clements_Bath_Invitational_Mens_5000_Meters_Class_1_24.csv"
csv_file3 = "meets/SEC_Jamboree_#1_Mens_5000_Meters_Junior_Varsity_24.csv"


# Change .html file name here !!
html1_file = "meet1.html"
html2_file = "meet2.html"
html3_file = "meet3.html"


# Function to get the next non-blank row
def get_next_non_blank(reader):
    for row in reader:
        if any(cell.strip() for cell in row):  # Check if any non-empty cells exist
            return row
    return None  # In case all remaining rows are blank

def csv_to_html(csv_file, html_file):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)   

    # Read header information
        meet_name = get_next_non_blank(reader)
        meet_date = get_next_non_blank(reader)
        meet_link = get_next_non_blank(reader)
        meet_description = get_next_non_blank(reader)
        headers1 = get_next_non_blank(reader)

    # Start building the HTML content
        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{meet_name[0]} Meet Scores</title>
        </head>
        <body>
            <header>
                <h1> Welcome to Skyline High
            </header>
            <main>

                <h1>{meet_name[0]} Meet Scores</h1>
                <h2>{meet_date[0]}</h2>
                <h3>{meet_description[0]}</h3>
                <a href="{meet_link[0]}">Meet Link</a>
                <h3>Team Scores:</h3>
                <table class="team_scores" border="1">
                    <tr>
            </main>
        """

    # Add headers to the HTML table for team scores
        for header in headers1:
            html_content += f"<th>{header}</th>"
        html_content += "</tr>"

    # Process the rows and handle the second table (Athlete Scores) when the "Place" header is encountered
        for row in reader:
            if row and row[0].strip() == "Place":
                # End first table, begin second table
                html_content += """
                </table>
                <h3>Athlete Scores:</h3>
                <table class="athlete_scores" border="1">
                """
                # Get the new headers for the second table
                headers2 = row
                html_content += "<tr>"
                for header in headers2:
                    html_content += f"<th>{header}</th>"
                html_content += "</tr>"
            else:
                if row:
                    html_content += "<tr>"
                    for item in row:
                        html_content += f"<td>{item}</td>"
                    html_content += "</tr>"

    # End the HTML content
        html_content += """
            </table>
        </body>
        </html>
        """

# Write the HTML content to the output file
    with open(html_file, 'w') as f:
        f.write(html_content)

    print(f"HTML file has been successfully generated: {html1_file}")

csv_to_html(csv_file1, html1_file)
csv_to_html(csv_file2, html2_file)
csv_to_html(csv_file3, html3_file)