DROP TABLE IF EXISTS "События";

CREATE TABLE "События" (
  id          BIGSERIAL PRIMARY KEY,
  "timestamp" TIMESTAMPTZ NOT NULL DEFAULT now(),
  "игрок"     TEXT NOT NULL,
  "действие"  TEXT NOT NULL,
  "очки"      INT  NOT NULL,
  "уровень"   INT  NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_events_player ON "События" ("игрок");
CREATE INDEX IF NOT EXISTS idx_events_action ON "События" ("действие");
CREATE INDEX IF NOT EXISTS idx_events_level  ON "События" ("уровень");
CREATE INDEX IF NOT EXISTS idx_events_ts     ON "События" ("timestamp");