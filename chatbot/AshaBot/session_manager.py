# Session context handling
import uuid

class SessionManager:
    def _init_(self):
        self.sessions = {}  # Store session data {session_id: {"last_query": str, "last_response": list}}

    def start_session(self):
        session_id = str(uuid.uuid4())  # Generate unique session ID
        self.sessions[session_id] = {"last_query": "", "last_response": []}
        return session_id

    def update_session(self, session_id, query, response):
        if session_id in self.sessions:
            self.sessions[session_id]["last_query"] = query
            self.sessions[session_id]["last_response"] = response

    def get_session(self, session_id):
        return self.sessions.get(session_id, {"last_query": "", "last_response": []})

    def clear_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]