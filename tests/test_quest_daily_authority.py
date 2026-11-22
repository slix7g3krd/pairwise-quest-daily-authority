import pytest
import gameplay.quest_daily_authority as mod

CASES = [
    ("server_time", (1, 2)),
    ("idempotent_claim", (1, 2)),
    ("utc_boundary", (1, 2)),
    ("local_offset", (8, 2)),
    ("chain_prereq", (1, 2)),
    ("claim_token", (1, 2)),
    ("double_claim_guard", (1, 2)),
    ("reset_cross_day", (1, 2)),
    ("clock_skew", (60, 2)),
    ("reward_once", (1, 2)),
    ("offline_replay", (1, 2)),
    ("timezone_convert", (1, 2)),
    ("lock_account", (1, 2)),
    ("audit_log", (1, 2)),
    ("retry_check", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
