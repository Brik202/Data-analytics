DROP TABLE IF EXISTS "События";

CREATE TABLE "События" (
  "игрок"    TEXT NOT NULL,
  "действие" TEXT NOT NULL,
  "очки"     INT  NOT NULL,
  "уровень"  INT  NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_events_player ON "События" ("игрок");
CREATE INDEX IF NOT EXISTS idx_events_action ON "События" ("действие");
CREATE INDEX IF NOT EXISTS idx_events_level  ON "События" ("уровень");
