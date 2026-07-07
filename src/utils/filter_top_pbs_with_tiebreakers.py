from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
from models import Activity, Submission


def filter_top_pbs_with_tiebreakers(activity: Activity, submissions: list[Submission]):
    """
    ---Assumptions---
    Submissions is a sorted list in the intented order to display. It is pre-sorted by it's metric
    This is why I'm assigning best_metric to any new metric that shows up, to account for desc/asc
    """
    result = {
        "name": activity.activity_name,
        "emoji": activity.emoji,
        "placements_to_show": activity.placements_to_show,
        "placements": [{"submissions": []} for _ in range(activity.placements_to_show)],
        "is_time_based": activity.is_time_based,
    }

    if len(submissions) == 0:
        return result

    best_place_so_far = submissions[0].metric

    # Index stuff. 0 = starter for the algorithm. 0 = 1st place, 1 = 2nd place, 2 = 3rd place
    placement = 0

    for submission in range(len(submissions) - 1):
        if placement >= activity.placements_to_show:
            break

        result["placements"][placement]["submissions"].append(
            {
                "username": submissions[submission].players,
                "metric": submissions[submission].metric,
                "imgur_url": submissions[submission].imgur_url,
            }
        )
        if submissions[submission + 1].metric != best_place_so_far:
            placement += 1
            best_place_so_far = submissions[submission + 1].metric

    # cursor = 0
    # placement = 0
    # submission = submissions[0]
    # best_metric = submission.metric

    return result


# ----------------------------
# Unit Tests
# ----------------------------
given_submissions = [
    Submission(
        id=1,
        activity=1,
        players="user1",
        metric=95,
    ),
    Submission(id=2, activity=1, players="user2", metric=95),
    Submission(id=3, activity=1, players="user3", metric=95),
    Submission(id=4, activity=1, players="user4", metric=96),
    Submission(id=5, activity=1, players="user5", metric=96),
    Submission(id=6, activity=1, players="user6", metric=96),
    Submission(id=7, activity=1, players="user7", metric=98),
    Submission(id=8, activity=1, players="user8", metric=99),
    Submission(id=9, activity=1, players="user8", metric=121),
    Submission(id=10, activity=1, players="user8", metric=122),
    Submission(id=11, activity=1, players="user8", metric=125),
    Submission(id=12, activity=1, players="user8", metric=126),
]
given_activity = Activity(
    id=1, activity_name="Zulrah", is_time_based=True, placements_to_show=3
)

expected_result = {
    "name": "Zulrah",
    "emoji": None,
    "placements_to_show": 3,
    "placements": [
        {
            "submissions": [
                {"username": "user1", "imgur_url": None, "metric": 95},
                {"username": "user2", "imgur_url": None, "metric": 95},
                {"username": "user3", "imgur_url": None, "metric": 95},
            ],
        },
        {
            "submissions": [
                {"username": "user4", "imgur_url": None, "metric": 96},
                {"username": "user5", "imgur_url": None, "metric": 96},
                {"username": "user6", "imgur_url": None, "metric": 96},
            ]
        },
        {"submissions": [{"username": "user7", "imgur_url": None, "metric": 98}]},
    ],
    "is_time_based": True,
}

test = filter_top_pbs_with_tiebreakers(given_activity, given_submissions)

assert test == expected_result
