import csv
import os

def analyze_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            reader.fieldnames = [field.strip() for field in reader.fieldnames]
            data = list(reader)
            
            if not data:
                print("No data found in CSV.")
                return

            total_youtubers = len(data)

            # Use the correct column names from the combined CSV
            sub_col = 'total_subscribers'
            views_col = 'total_views'
            videos_col = 'total_videos'
            name_col = 'channel_name'

            # Clean and convert data
            for row in data:
                try:
                    row[sub_col] = int(float(row.get(sub_col, 0)))
                    row[views_col] = int(float(row.get(views_col, 0)))
                    row[videos_col] = int(float(row.get(videos_col, 0)))
                except (ValueError, TypeError):
                    row[sub_col] = 0
                    row[views_col] = 0
                    row[videos_col] = 0

            top_by_subs = max(data, key=lambda x: x.get(sub_col, 0))
            top_by_views = max(data, key=lambda x: x.get(views_col, 0))
            top_by_videos = max(data, key=lambda x: x.get(videos_col, 0))

            print(f"Total YouTubers: {total_youtubers}")
            print(f"Top by Subscribers: {top_by_subs[name_col]} with {top_by_subs[sub_col]:,} subscribers")
            print(f"Top by Views: {top_by_views[name_col]} with {top_by_views[views_col]:,} views")
            print(f"Top by Videos: {top_by_videos[name_col]} with {top_by_videos[videos_col]:,} videos")

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Use the correct CSV file with the combined and cleaned data
    file_to_analyze = os.path.join("assets", "datasets", "youtube_data_from_python.csv")
    analyze_csv(file_to_analyze)