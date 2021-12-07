-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "country" (
    "countryid" int   NOT NULL,
    "code" varchar   NOT NULL,
    "country" varchar   NOT NULL,
    "region" varchar   NOT NULL,
    CONSTRAINT "pk_country" PRIMARY KEY (
        "code"
     )
);

CREATE TABLE "measures" (
    "measuresid" int   NOT NULL,
    "code" varchar   NOT NULL,
    "freedom_2021" float   NOT NULL,
    "generosity_2021" float   NOT NULL,
    "corruption_2021" float   NOT NULL,
    "freedom_2019" float   NOT NULL,
    "generosity_2019" float   NOT NULL,
    "corruption_2019" float   NOT NULL,
    CONSTRAINT "pk_measures" PRIMARY KEY (
        "code"
     )
);

CREATE TABLE "happiness" (
    "happinessid" int   NOT NULL,
    "code" varchar   NOT NULL,
    "happiness_score_2021" float   NOT NULL,
    "sd_happiness_score_2021" float   NOT NULL,
    "happiness_score_2019" float   NOT NULL,
    "sd_happiness_score_2019" float   NOT NULL,
    CONSTRAINT "pk_happiness" PRIMARY KEY (
        "code"
     )
);

ALTER TABLE "measures" ADD CONSTRAINT "fk_measures_code" FOREIGN KEY("code")
REFERENCES "country" ("code");

ALTER TABLE "happiness" ADD CONSTRAINT "fk_happiness_code" FOREIGN KEY("code")
REFERENCES "country" ("code");

