class DisputeContract:
    def __init__(self):
        self.disputes = {}

    def create_dispute(self, dispute_id, claimant, respondent):
        self.disputes[dispute_id] = {
            "claimant": claimant,
            "respondent": respondent,
            "status": "pending"
        }

    def resolve_dispute(self, dispute_id, winner, reason):
        self.disputes[dispute_id]["status"] = "resolved"
        self.disputes[dispute_id]["winner"] = winner
        self.disputes[dispute_id]["reason"] = reason

        return {
            "winner": winner,
            "reason": reason
        }
