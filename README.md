# pairwise-quest-daily-authority

## 领域

游戏、图形与多媒体

## 主题

任务跨天权威

## 说明

服务端时间、领取幂等与 UTC 跨天切分。

初始状态下 `gameplay/quest_daily_authority.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
