#loading and query
import pandas as pd

class DataRetriever:
    def __init__(self, file_path):
        self.file_path = file_path

    def search(self, query, session_data):
        return [f"Result for '{query} '"]
        self.df[self.df.apply(lambda row:
        query.lower() in str(row).lower(),axis=1)].to_dict(orient="records")

        if "remote" in query.lower() and last_response:
            results = [r for r in last_response if "Remote" in r.get("location", "")]
        else:
            query = query.lower()
            results = self.df[
                self.df["job_title"].str.lower().str.contains(query) |
                self.df["category"].str.lower().str.contains(query)
            ].to_dict("records")

        # Save current query and results in session
        session_data["last_query"] = query
        session_data["last_response"] = results

        if not results:
            return [{"job_title": "No results found", "category": "", "location": ""}]
        return results
       