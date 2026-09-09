export interface CPTEntry {
  cptCode: string;
  shortDesc: string;
  longDesc: string;
  category: string;
  workRvu: number;
  facilityRvu: number;
  prerequisites: string[];
}

export const CPT_DATABASE: Record<string, CPTEntry> = {
  "93001": {
    cptCode: "93001",
    shortDesc: "Cardiology Procedure Tier 1",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 1.",
    category: "Cardiology",
    workRvu: 1.3,
    facilityRvu: 4.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93002": {
    cptCode: "93002",
    shortDesc: "Cardiology Procedure Tier 2",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 2.",
    category: "Cardiology",
    workRvu: 1.35,
    facilityRvu: 4.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93003": {
    cptCode: "93003",
    shortDesc: "Cardiology Procedure Tier 3",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 3.",
    category: "Cardiology",
    workRvu: 1.4,
    facilityRvu: 4.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93004": {
    cptCode: "93004",
    shortDesc: "Cardiology Procedure Tier 4",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 4.",
    category: "Cardiology",
    workRvu: 1.45,
    facilityRvu: 5.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93005": {
    cptCode: "93005",
    shortDesc: "Cardiology Procedure Tier 5",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 5.",
    category: "Cardiology",
    workRvu: 1.5,
    facilityRvu: 5.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93006": {
    cptCode: "93006",
    shortDesc: "Cardiology Procedure Tier 6",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 6.",
    category: "Cardiology",
    workRvu: 1.55,
    facilityRvu: 5.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93007": {
    cptCode: "93007",
    shortDesc: "Cardiology Procedure Tier 7",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 7.",
    category: "Cardiology",
    workRvu: 1.6,
    facilityRvu: 5.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93008": {
    cptCode: "93008",
    shortDesc: "Cardiology Procedure Tier 8",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 8.",
    category: "Cardiology",
    workRvu: 1.65,
    facilityRvu: 5.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93009": {
    cptCode: "93009",
    shortDesc: "Cardiology Procedure Tier 9",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 9.",
    category: "Cardiology",
    workRvu: 1.7,
    facilityRvu: 5.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93010": {
    cptCode: "93010",
    shortDesc: "Cardiology Procedure Tier 10",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 10.",
    category: "Cardiology",
    workRvu: 1.75,
    facilityRvu: 6.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93011": {
    cptCode: "93011",
    shortDesc: "Cardiology Procedure Tier 11",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 11.",
    category: "Cardiology",
    workRvu: 1.8,
    facilityRvu: 6.15,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93012": {
    cptCode: "93012",
    shortDesc: "Cardiology Procedure Tier 12",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 12.",
    category: "Cardiology",
    workRvu: 1.85,
    facilityRvu: 6.3,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93013": {
    cptCode: "93013",
    shortDesc: "Cardiology Procedure Tier 13",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 13.",
    category: "Cardiology",
    workRvu: 1.9,
    facilityRvu: 6.45,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93014": {
    cptCode: "93014",
    shortDesc: "Cardiology Procedure Tier 14",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 14.",
    category: "Cardiology",
    workRvu: 1.95,
    facilityRvu: 6.6,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93015": {
    cptCode: "93015",
    shortDesc: "Cardiology Procedure Tier 15",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 15.",
    category: "Cardiology",
    workRvu: 2.0,
    facilityRvu: 6.75,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93016": {
    cptCode: "93016",
    shortDesc: "Cardiology Procedure Tier 16",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 16.",
    category: "Cardiology",
    workRvu: 2.05,
    facilityRvu: 6.9,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93017": {
    cptCode: "93017",
    shortDesc: "Cardiology Procedure Tier 17",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 17.",
    category: "Cardiology",
    workRvu: 2.1,
    facilityRvu: 7.05,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93018": {
    cptCode: "93018",
    shortDesc: "Cardiology Procedure Tier 18",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 18.",
    category: "Cardiology",
    workRvu: 2.15,
    facilityRvu: 7.2,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93019": {
    cptCode: "93019",
    shortDesc: "Cardiology Procedure Tier 19",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 19.",
    category: "Cardiology",
    workRvu: 2.2,
    facilityRvu: 7.35,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93020": {
    cptCode: "93020",
    shortDesc: "Cardiology Procedure Tier 20",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 20.",
    category: "Cardiology",
    workRvu: 2.25,
    facilityRvu: 7.5,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93021": {
    cptCode: "93021",
    shortDesc: "Cardiology Procedure Tier 21",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 21.",
    category: "Cardiology",
    workRvu: 2.3,
    facilityRvu: 7.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93022": {
    cptCode: "93022",
    shortDesc: "Cardiology Procedure Tier 22",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 22.",
    category: "Cardiology",
    workRvu: 2.35,
    facilityRvu: 7.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93023": {
    cptCode: "93023",
    shortDesc: "Cardiology Procedure Tier 23",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 23.",
    category: "Cardiology",
    workRvu: 2.4,
    facilityRvu: 7.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93024": {
    cptCode: "93024",
    shortDesc: "Cardiology Procedure Tier 24",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 24.",
    category: "Cardiology",
    workRvu: 2.45,
    facilityRvu: 8.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93025": {
    cptCode: "93025",
    shortDesc: "Cardiology Procedure Tier 25",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 25.",
    category: "Cardiology",
    workRvu: 2.5,
    facilityRvu: 8.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93026": {
    cptCode: "93026",
    shortDesc: "Cardiology Procedure Tier 26",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 26.",
    category: "Cardiology",
    workRvu: 2.55,
    facilityRvu: 8.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93027": {
    cptCode: "93027",
    shortDesc: "Cardiology Procedure Tier 27",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 27.",
    category: "Cardiology",
    workRvu: 2.6,
    facilityRvu: 8.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93028": {
    cptCode: "93028",
    shortDesc: "Cardiology Procedure Tier 28",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 28.",
    category: "Cardiology",
    workRvu: 2.65,
    facilityRvu: 8.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93029": {
    cptCode: "93029",
    shortDesc: "Cardiology Procedure Tier 29",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 29.",
    category: "Cardiology",
    workRvu: 2.7,
    facilityRvu: 8.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "93030": {
    cptCode: "93030",
    shortDesc: "Cardiology Procedure Tier 30",
    longDesc: "Diagnostic and therapeutic intervention in cardiology medicine, level 30.",
    category: "Cardiology",
    workRvu: 2.75,
    facilityRvu: 9.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71001": {
    cptCode: "71001",
    shortDesc: "Radiology Procedure Tier 1",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 1.",
    category: "Radiology",
    workRvu: 0.9,
    facilityRvu: 3.35,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71002": {
    cptCode: "71002",
    shortDesc: "Radiology Procedure Tier 2",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 2.",
    category: "Radiology",
    workRvu: 0.95,
    facilityRvu: 3.5,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71003": {
    cptCode: "71003",
    shortDesc: "Radiology Procedure Tier 3",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 3.",
    category: "Radiology",
    workRvu: 1.0,
    facilityRvu: 3.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71004": {
    cptCode: "71004",
    shortDesc: "Radiology Procedure Tier 4",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 4.",
    category: "Radiology",
    workRvu: 1.05,
    facilityRvu: 3.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71005": {
    cptCode: "71005",
    shortDesc: "Radiology Procedure Tier 5",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 5.",
    category: "Radiology",
    workRvu: 1.1,
    facilityRvu: 3.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71006": {
    cptCode: "71006",
    shortDesc: "Radiology Procedure Tier 6",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 6.",
    category: "Radiology",
    workRvu: 1.15,
    facilityRvu: 4.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71007": {
    cptCode: "71007",
    shortDesc: "Radiology Procedure Tier 7",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 7.",
    category: "Radiology",
    workRvu: 1.2,
    facilityRvu: 4.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71008": {
    cptCode: "71008",
    shortDesc: "Radiology Procedure Tier 8",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 8.",
    category: "Radiology",
    workRvu: 1.25,
    facilityRvu: 4.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71009": {
    cptCode: "71009",
    shortDesc: "Radiology Procedure Tier 9",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 9.",
    category: "Radiology",
    workRvu: 1.3,
    facilityRvu: 4.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71010": {
    cptCode: "71010",
    shortDesc: "Radiology Procedure Tier 10",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 10.",
    category: "Radiology",
    workRvu: 1.35,
    facilityRvu: 4.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71011": {
    cptCode: "71011",
    shortDesc: "Radiology Procedure Tier 11",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 11.",
    category: "Radiology",
    workRvu: 1.4,
    facilityRvu: 4.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71012": {
    cptCode: "71012",
    shortDesc: "Radiology Procedure Tier 12",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 12.",
    category: "Radiology",
    workRvu: 1.45,
    facilityRvu: 5.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71013": {
    cptCode: "71013",
    shortDesc: "Radiology Procedure Tier 13",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 13.",
    category: "Radiology",
    workRvu: 1.5,
    facilityRvu: 5.15,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71014": {
    cptCode: "71014",
    shortDesc: "Radiology Procedure Tier 14",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 14.",
    category: "Radiology",
    workRvu: 1.55,
    facilityRvu: 5.3,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71015": {
    cptCode: "71015",
    shortDesc: "Radiology Procedure Tier 15",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 15.",
    category: "Radiology",
    workRvu: 1.6,
    facilityRvu: 5.45,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71016": {
    cptCode: "71016",
    shortDesc: "Radiology Procedure Tier 16",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 16.",
    category: "Radiology",
    workRvu: 1.65,
    facilityRvu: 5.6,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71017": {
    cptCode: "71017",
    shortDesc: "Radiology Procedure Tier 17",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 17.",
    category: "Radiology",
    workRvu: 1.7,
    facilityRvu: 5.75,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71018": {
    cptCode: "71018",
    shortDesc: "Radiology Procedure Tier 18",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 18.",
    category: "Radiology",
    workRvu: 1.75,
    facilityRvu: 5.9,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71019": {
    cptCode: "71019",
    shortDesc: "Radiology Procedure Tier 19",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 19.",
    category: "Radiology",
    workRvu: 1.8,
    facilityRvu: 6.05,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71020": {
    cptCode: "71020",
    shortDesc: "Radiology Procedure Tier 20",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 20.",
    category: "Radiology",
    workRvu: 1.85,
    facilityRvu: 6.2,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71021": {
    cptCode: "71021",
    shortDesc: "Radiology Procedure Tier 21",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 21.",
    category: "Radiology",
    workRvu: 1.9,
    facilityRvu: 6.35,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71022": {
    cptCode: "71022",
    shortDesc: "Radiology Procedure Tier 22",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 22.",
    category: "Radiology",
    workRvu: 1.95,
    facilityRvu: 6.5,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71023": {
    cptCode: "71023",
    shortDesc: "Radiology Procedure Tier 23",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 23.",
    category: "Radiology",
    workRvu: 2.0,
    facilityRvu: 6.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71024": {
    cptCode: "71024",
    shortDesc: "Radiology Procedure Tier 24",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 24.",
    category: "Radiology",
    workRvu: 2.05,
    facilityRvu: 6.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71025": {
    cptCode: "71025",
    shortDesc: "Radiology Procedure Tier 25",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 25.",
    category: "Radiology",
    workRvu: 2.1,
    facilityRvu: 6.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71026": {
    cptCode: "71026",
    shortDesc: "Radiology Procedure Tier 26",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 26.",
    category: "Radiology",
    workRvu: 2.15,
    facilityRvu: 7.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71027": {
    cptCode: "71027",
    shortDesc: "Radiology Procedure Tier 27",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 27.",
    category: "Radiology",
    workRvu: 2.2,
    facilityRvu: 7.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71028": {
    cptCode: "71028",
    shortDesc: "Radiology Procedure Tier 28",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 28.",
    category: "Radiology",
    workRvu: 2.25,
    facilityRvu: 7.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71029": {
    cptCode: "71029",
    shortDesc: "Radiology Procedure Tier 29",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 29.",
    category: "Radiology",
    workRvu: 2.3,
    facilityRvu: 7.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "71030": {
    cptCode: "71030",
    shortDesc: "Radiology Procedure Tier 30",
    longDesc: "Diagnostic and therapeutic intervention in radiology medicine, level 30.",
    category: "Radiology",
    workRvu: 2.35,
    facilityRvu: 7.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80054": {
    cptCode: "80054",
    shortDesc: "Laboratory Procedure Tier 1",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 1.",
    category: "Laboratory",
    workRvu: 0.4,
    facilityRvu: 1.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80055": {
    cptCode: "80055",
    shortDesc: "Laboratory Procedure Tier 2",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 2.",
    category: "Laboratory",
    workRvu: 0.45,
    facilityRvu: 1.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80056": {
    cptCode: "80056",
    shortDesc: "Laboratory Procedure Tier 3",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 3.",
    category: "Laboratory",
    workRvu: 0.5,
    facilityRvu: 1.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80057": {
    cptCode: "80057",
    shortDesc: "Laboratory Procedure Tier 4",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 4.",
    category: "Laboratory",
    workRvu: 0.55,
    facilityRvu: 1.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80058": {
    cptCode: "80058",
    shortDesc: "Laboratory Procedure Tier 5",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 5.",
    category: "Laboratory",
    workRvu: 0.6,
    facilityRvu: 1.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80059": {
    cptCode: "80059",
    shortDesc: "Laboratory Procedure Tier 6",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 6.",
    category: "Laboratory",
    workRvu: 0.65,
    facilityRvu: 2.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80060": {
    cptCode: "80060",
    shortDesc: "Laboratory Procedure Tier 7",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 7.",
    category: "Laboratory",
    workRvu: 0.7,
    facilityRvu: 2.15,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80061": {
    cptCode: "80061",
    shortDesc: "Laboratory Procedure Tier 8",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 8.",
    category: "Laboratory",
    workRvu: 0.75,
    facilityRvu: 2.3,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80062": {
    cptCode: "80062",
    shortDesc: "Laboratory Procedure Tier 9",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 9.",
    category: "Laboratory",
    workRvu: 0.8,
    facilityRvu: 2.45,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80063": {
    cptCode: "80063",
    shortDesc: "Laboratory Procedure Tier 10",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 10.",
    category: "Laboratory",
    workRvu: 0.85,
    facilityRvu: 2.6,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80064": {
    cptCode: "80064",
    shortDesc: "Laboratory Procedure Tier 11",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 11.",
    category: "Laboratory",
    workRvu: 0.9,
    facilityRvu: 2.75,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80065": {
    cptCode: "80065",
    shortDesc: "Laboratory Procedure Tier 12",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 12.",
    category: "Laboratory",
    workRvu: 0.95,
    facilityRvu: 2.9,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80066": {
    cptCode: "80066",
    shortDesc: "Laboratory Procedure Tier 13",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 13.",
    category: "Laboratory",
    workRvu: 1.0,
    facilityRvu: 3.05,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80067": {
    cptCode: "80067",
    shortDesc: "Laboratory Procedure Tier 14",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 14.",
    category: "Laboratory",
    workRvu: 1.05,
    facilityRvu: 3.2,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80068": {
    cptCode: "80068",
    shortDesc: "Laboratory Procedure Tier 15",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 15.",
    category: "Laboratory",
    workRvu: 1.1,
    facilityRvu: 3.35,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80069": {
    cptCode: "80069",
    shortDesc: "Laboratory Procedure Tier 16",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 16.",
    category: "Laboratory",
    workRvu: 1.15,
    facilityRvu: 3.5,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80070": {
    cptCode: "80070",
    shortDesc: "Laboratory Procedure Tier 17",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 17.",
    category: "Laboratory",
    workRvu: 1.2,
    facilityRvu: 3.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80071": {
    cptCode: "80071",
    shortDesc: "Laboratory Procedure Tier 18",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 18.",
    category: "Laboratory",
    workRvu: 1.25,
    facilityRvu: 3.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80072": {
    cptCode: "80072",
    shortDesc: "Laboratory Procedure Tier 19",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 19.",
    category: "Laboratory",
    workRvu: 1.3,
    facilityRvu: 3.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80073": {
    cptCode: "80073",
    shortDesc: "Laboratory Procedure Tier 20",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 20.",
    category: "Laboratory",
    workRvu: 1.35,
    facilityRvu: 4.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80074": {
    cptCode: "80074",
    shortDesc: "Laboratory Procedure Tier 21",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 21.",
    category: "Laboratory",
    workRvu: 1.4,
    facilityRvu: 4.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80075": {
    cptCode: "80075",
    shortDesc: "Laboratory Procedure Tier 22",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 22.",
    category: "Laboratory",
    workRvu: 1.45,
    facilityRvu: 4.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80076": {
    cptCode: "80076",
    shortDesc: "Laboratory Procedure Tier 23",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 23.",
    category: "Laboratory",
    workRvu: 1.5,
    facilityRvu: 4.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80077": {
    cptCode: "80077",
    shortDesc: "Laboratory Procedure Tier 24",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 24.",
    category: "Laboratory",
    workRvu: 1.55,
    facilityRvu: 4.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80078": {
    cptCode: "80078",
    shortDesc: "Laboratory Procedure Tier 25",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 25.",
    category: "Laboratory",
    workRvu: 1.6,
    facilityRvu: 4.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80079": {
    cptCode: "80079",
    shortDesc: "Laboratory Procedure Tier 26",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 26.",
    category: "Laboratory",
    workRvu: 1.65,
    facilityRvu: 5.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80080": {
    cptCode: "80080",
    shortDesc: "Laboratory Procedure Tier 27",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 27.",
    category: "Laboratory",
    workRvu: 1.7,
    facilityRvu: 5.15,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80081": {
    cptCode: "80081",
    shortDesc: "Laboratory Procedure Tier 28",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 28.",
    category: "Laboratory",
    workRvu: 1.75,
    facilityRvu: 5.3,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80082": {
    cptCode: "80082",
    shortDesc: "Laboratory Procedure Tier 29",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 29.",
    category: "Laboratory",
    workRvu: 1.8,
    facilityRvu: 5.45,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "80083": {
    cptCode: "80083",
    shortDesc: "Laboratory Procedure Tier 30",
    longDesc: "Diagnostic and therapeutic intervention in laboratory medicine, level 30.",
    category: "Laboratory",
    workRvu: 1.85,
    facilityRvu: 5.6,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94011": {
    cptCode: "94011",
    shortDesc: "Pulmonary Procedure Tier 1",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 1.",
    category: "Pulmonary",
    workRvu: 0.7,
    facilityRvu: 2.45,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94012": {
    cptCode: "94012",
    shortDesc: "Pulmonary Procedure Tier 2",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 2.",
    category: "Pulmonary",
    workRvu: 0.75,
    facilityRvu: 2.6,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94013": {
    cptCode: "94013",
    shortDesc: "Pulmonary Procedure Tier 3",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 3.",
    category: "Pulmonary",
    workRvu: 0.8,
    facilityRvu: 2.75,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94014": {
    cptCode: "94014",
    shortDesc: "Pulmonary Procedure Tier 4",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 4.",
    category: "Pulmonary",
    workRvu: 0.85,
    facilityRvu: 2.9,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94015": {
    cptCode: "94015",
    shortDesc: "Pulmonary Procedure Tier 5",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 5.",
    category: "Pulmonary",
    workRvu: 0.9,
    facilityRvu: 3.05,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94016": {
    cptCode: "94016",
    shortDesc: "Pulmonary Procedure Tier 6",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 6.",
    category: "Pulmonary",
    workRvu: 0.95,
    facilityRvu: 3.2,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94017": {
    cptCode: "94017",
    shortDesc: "Pulmonary Procedure Tier 7",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 7.",
    category: "Pulmonary",
    workRvu: 1.0,
    facilityRvu: 3.35,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94018": {
    cptCode: "94018",
    shortDesc: "Pulmonary Procedure Tier 8",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 8.",
    category: "Pulmonary",
    workRvu: 1.05,
    facilityRvu: 3.5,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94019": {
    cptCode: "94019",
    shortDesc: "Pulmonary Procedure Tier 9",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 9.",
    category: "Pulmonary",
    workRvu: 1.1,
    facilityRvu: 3.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94020": {
    cptCode: "94020",
    shortDesc: "Pulmonary Procedure Tier 10",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 10.",
    category: "Pulmonary",
    workRvu: 1.15,
    facilityRvu: 3.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94021": {
    cptCode: "94021",
    shortDesc: "Pulmonary Procedure Tier 11",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 11.",
    category: "Pulmonary",
    workRvu: 1.2,
    facilityRvu: 3.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94022": {
    cptCode: "94022",
    shortDesc: "Pulmonary Procedure Tier 12",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 12.",
    category: "Pulmonary",
    workRvu: 1.25,
    facilityRvu: 4.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94023": {
    cptCode: "94023",
    shortDesc: "Pulmonary Procedure Tier 13",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 13.",
    category: "Pulmonary",
    workRvu: 1.3,
    facilityRvu: 4.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94024": {
    cptCode: "94024",
    shortDesc: "Pulmonary Procedure Tier 14",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 14.",
    category: "Pulmonary",
    workRvu: 1.35,
    facilityRvu: 4.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94025": {
    cptCode: "94025",
    shortDesc: "Pulmonary Procedure Tier 15",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 15.",
    category: "Pulmonary",
    workRvu: 1.4,
    facilityRvu: 4.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94026": {
    cptCode: "94026",
    shortDesc: "Pulmonary Procedure Tier 16",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 16.",
    category: "Pulmonary",
    workRvu: 1.45,
    facilityRvu: 4.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94027": {
    cptCode: "94027",
    shortDesc: "Pulmonary Procedure Tier 17",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 17.",
    category: "Pulmonary",
    workRvu: 1.5,
    facilityRvu: 4.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94028": {
    cptCode: "94028",
    shortDesc: "Pulmonary Procedure Tier 18",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 18.",
    category: "Pulmonary",
    workRvu: 1.55,
    facilityRvu: 5.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94029": {
    cptCode: "94029",
    shortDesc: "Pulmonary Procedure Tier 19",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 19.",
    category: "Pulmonary",
    workRvu: 1.6,
    facilityRvu: 5.15,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94030": {
    cptCode: "94030",
    shortDesc: "Pulmonary Procedure Tier 20",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 20.",
    category: "Pulmonary",
    workRvu: 1.65,
    facilityRvu: 5.3,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94031": {
    cptCode: "94031",
    shortDesc: "Pulmonary Procedure Tier 21",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 21.",
    category: "Pulmonary",
    workRvu: 1.7,
    facilityRvu: 5.45,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94032": {
    cptCode: "94032",
    shortDesc: "Pulmonary Procedure Tier 22",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 22.",
    category: "Pulmonary",
    workRvu: 1.75,
    facilityRvu: 5.6,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94033": {
    cptCode: "94033",
    shortDesc: "Pulmonary Procedure Tier 23",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 23.",
    category: "Pulmonary",
    workRvu: 1.8,
    facilityRvu: 5.75,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94034": {
    cptCode: "94034",
    shortDesc: "Pulmonary Procedure Tier 24",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 24.",
    category: "Pulmonary",
    workRvu: 1.85,
    facilityRvu: 5.9,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94035": {
    cptCode: "94035",
    shortDesc: "Pulmonary Procedure Tier 25",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 25.",
    category: "Pulmonary",
    workRvu: 1.9,
    facilityRvu: 6.05,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94036": {
    cptCode: "94036",
    shortDesc: "Pulmonary Procedure Tier 26",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 26.",
    category: "Pulmonary",
    workRvu: 1.95,
    facilityRvu: 6.2,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94037": {
    cptCode: "94037",
    shortDesc: "Pulmonary Procedure Tier 27",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 27.",
    category: "Pulmonary",
    workRvu: 2.0,
    facilityRvu: 6.35,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94038": {
    cptCode: "94038",
    shortDesc: "Pulmonary Procedure Tier 28",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 28.",
    category: "Pulmonary",
    workRvu: 2.05,
    facilityRvu: 6.5,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94039": {
    cptCode: "94039",
    shortDesc: "Pulmonary Procedure Tier 29",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 29.",
    category: "Pulmonary",
    workRvu: 2.1,
    facilityRvu: 6.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "94040": {
    cptCode: "94040",
    shortDesc: "Pulmonary Procedure Tier 30",
    longDesc: "Diagnostic and therapeutic intervention in pulmonary medicine, level 30.",
    category: "Pulmonary",
    workRvu: 2.15,
    facilityRvu: 6.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43236": {
    cptCode: "43236",
    shortDesc: "Gastroenterology Procedure Tier 1",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 1.",
    category: "Gastroenterology",
    workRvu: 2.15,
    facilityRvu: 6.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43237": {
    cptCode: "43237",
    shortDesc: "Gastroenterology Procedure Tier 2",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 2.",
    category: "Gastroenterology",
    workRvu: 2.2,
    facilityRvu: 7.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43238": {
    cptCode: "43238",
    shortDesc: "Gastroenterology Procedure Tier 3",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 3.",
    category: "Gastroenterology",
    workRvu: 2.25,
    facilityRvu: 7.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43239": {
    cptCode: "43239",
    shortDesc: "Gastroenterology Procedure Tier 4",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 4.",
    category: "Gastroenterology",
    workRvu: 2.3,
    facilityRvu: 7.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43240": {
    cptCode: "43240",
    shortDesc: "Gastroenterology Procedure Tier 5",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 5.",
    category: "Gastroenterology",
    workRvu: 2.35,
    facilityRvu: 7.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43241": {
    cptCode: "43241",
    shortDesc: "Gastroenterology Procedure Tier 6",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 6.",
    category: "Gastroenterology",
    workRvu: 2.4,
    facilityRvu: 7.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43242": {
    cptCode: "43242",
    shortDesc: "Gastroenterology Procedure Tier 7",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 7.",
    category: "Gastroenterology",
    workRvu: 2.45,
    facilityRvu: 7.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43243": {
    cptCode: "43243",
    shortDesc: "Gastroenterology Procedure Tier 8",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 8.",
    category: "Gastroenterology",
    workRvu: 2.5,
    facilityRvu: 8.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43244": {
    cptCode: "43244",
    shortDesc: "Gastroenterology Procedure Tier 9",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 9.",
    category: "Gastroenterology",
    workRvu: 2.55,
    facilityRvu: 8.15,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43245": {
    cptCode: "43245",
    shortDesc: "Gastroenterology Procedure Tier 10",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 10.",
    category: "Gastroenterology",
    workRvu: 2.6,
    facilityRvu: 8.3,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43246": {
    cptCode: "43246",
    shortDesc: "Gastroenterology Procedure Tier 11",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 11.",
    category: "Gastroenterology",
    workRvu: 2.65,
    facilityRvu: 8.45,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43247": {
    cptCode: "43247",
    shortDesc: "Gastroenterology Procedure Tier 12",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 12.",
    category: "Gastroenterology",
    workRvu: 2.7,
    facilityRvu: 8.6,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43248": {
    cptCode: "43248",
    shortDesc: "Gastroenterology Procedure Tier 13",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 13.",
    category: "Gastroenterology",
    workRvu: 2.75,
    facilityRvu: 8.75,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43249": {
    cptCode: "43249",
    shortDesc: "Gastroenterology Procedure Tier 14",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 14.",
    category: "Gastroenterology",
    workRvu: 2.8,
    facilityRvu: 8.9,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43250": {
    cptCode: "43250",
    shortDesc: "Gastroenterology Procedure Tier 15",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 15.",
    category: "Gastroenterology",
    workRvu: 2.85,
    facilityRvu: 9.05,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43251": {
    cptCode: "43251",
    shortDesc: "Gastroenterology Procedure Tier 16",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 16.",
    category: "Gastroenterology",
    workRvu: 2.9,
    facilityRvu: 9.2,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43252": {
    cptCode: "43252",
    shortDesc: "Gastroenterology Procedure Tier 17",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 17.",
    category: "Gastroenterology",
    workRvu: 2.95,
    facilityRvu: 9.35,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43253": {
    cptCode: "43253",
    shortDesc: "Gastroenterology Procedure Tier 18",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 18.",
    category: "Gastroenterology",
    workRvu: 3.0,
    facilityRvu: 9.5,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43254": {
    cptCode: "43254",
    shortDesc: "Gastroenterology Procedure Tier 19",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 19.",
    category: "Gastroenterology",
    workRvu: 3.05,
    facilityRvu: 9.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43255": {
    cptCode: "43255",
    shortDesc: "Gastroenterology Procedure Tier 20",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 20.",
    category: "Gastroenterology",
    workRvu: 3.1,
    facilityRvu: 9.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43256": {
    cptCode: "43256",
    shortDesc: "Gastroenterology Procedure Tier 21",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 21.",
    category: "Gastroenterology",
    workRvu: 3.15,
    facilityRvu: 9.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43257": {
    cptCode: "43257",
    shortDesc: "Gastroenterology Procedure Tier 22",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 22.",
    category: "Gastroenterology",
    workRvu: 3.2,
    facilityRvu: 10.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43258": {
    cptCode: "43258",
    shortDesc: "Gastroenterology Procedure Tier 23",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 23.",
    category: "Gastroenterology",
    workRvu: 3.25,
    facilityRvu: 10.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43259": {
    cptCode: "43259",
    shortDesc: "Gastroenterology Procedure Tier 24",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 24.",
    category: "Gastroenterology",
    workRvu: 3.3,
    facilityRvu: 10.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43260": {
    cptCode: "43260",
    shortDesc: "Gastroenterology Procedure Tier 25",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 25.",
    category: "Gastroenterology",
    workRvu: 3.35,
    facilityRvu: 10.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43261": {
    cptCode: "43261",
    shortDesc: "Gastroenterology Procedure Tier 26",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 26.",
    category: "Gastroenterology",
    workRvu: 3.4,
    facilityRvu: 10.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43262": {
    cptCode: "43262",
    shortDesc: "Gastroenterology Procedure Tier 27",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 27.",
    category: "Gastroenterology",
    workRvu: 3.45,
    facilityRvu: 10.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43263": {
    cptCode: "43263",
    shortDesc: "Gastroenterology Procedure Tier 28",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 28.",
    category: "Gastroenterology",
    workRvu: 3.5,
    facilityRvu: 11.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43264": {
    cptCode: "43264",
    shortDesc: "Gastroenterology Procedure Tier 29",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 29.",
    category: "Gastroenterology",
    workRvu: 3.55,
    facilityRvu: 11.15,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "43265": {
    cptCode: "43265",
    shortDesc: "Gastroenterology Procedure Tier 30",
    longDesc: "Diagnostic and therapeutic intervention in gastroenterology medicine, level 30.",
    category: "Gastroenterology",
    workRvu: 3.6,
    facilityRvu: 11.3,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95811": {
    cptCode: "95811",
    shortDesc: "Neurology Procedure Tier 1",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 1.",
    category: "Neurology",
    workRvu: 1.8,
    facilityRvu: 5.35,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95812": {
    cptCode: "95812",
    shortDesc: "Neurology Procedure Tier 2",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 2.",
    category: "Neurology",
    workRvu: 1.85,
    facilityRvu: 5.5,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95813": {
    cptCode: "95813",
    shortDesc: "Neurology Procedure Tier 3",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 3.",
    category: "Neurology",
    workRvu: 1.9,
    facilityRvu: 5.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95814": {
    cptCode: "95814",
    shortDesc: "Neurology Procedure Tier 4",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 4.",
    category: "Neurology",
    workRvu: 1.95,
    facilityRvu: 5.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95815": {
    cptCode: "95815",
    shortDesc: "Neurology Procedure Tier 5",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 5.",
    category: "Neurology",
    workRvu: 2.0,
    facilityRvu: 5.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95816": {
    cptCode: "95816",
    shortDesc: "Neurology Procedure Tier 6",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 6.",
    category: "Neurology",
    workRvu: 2.05,
    facilityRvu: 6.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95817": {
    cptCode: "95817",
    shortDesc: "Neurology Procedure Tier 7",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 7.",
    category: "Neurology",
    workRvu: 2.1,
    facilityRvu: 6.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95818": {
    cptCode: "95818",
    shortDesc: "Neurology Procedure Tier 8",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 8.",
    category: "Neurology",
    workRvu: 2.15,
    facilityRvu: 6.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95819": {
    cptCode: "95819",
    shortDesc: "Neurology Procedure Tier 9",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 9.",
    category: "Neurology",
    workRvu: 2.2,
    facilityRvu: 6.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95820": {
    cptCode: "95820",
    shortDesc: "Neurology Procedure Tier 10",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 10.",
    category: "Neurology",
    workRvu: 2.25,
    facilityRvu: 6.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95821": {
    cptCode: "95821",
    shortDesc: "Neurology Procedure Tier 11",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 11.",
    category: "Neurology",
    workRvu: 2.3,
    facilityRvu: 6.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95822": {
    cptCode: "95822",
    shortDesc: "Neurology Procedure Tier 12",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 12.",
    category: "Neurology",
    workRvu: 2.35,
    facilityRvu: 7.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95823": {
    cptCode: "95823",
    shortDesc: "Neurology Procedure Tier 13",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 13.",
    category: "Neurology",
    workRvu: 2.4,
    facilityRvu: 7.15,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95824": {
    cptCode: "95824",
    shortDesc: "Neurology Procedure Tier 14",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 14.",
    category: "Neurology",
    workRvu: 2.45,
    facilityRvu: 7.3,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95825": {
    cptCode: "95825",
    shortDesc: "Neurology Procedure Tier 15",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 15.",
    category: "Neurology",
    workRvu: 2.5,
    facilityRvu: 7.45,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95826": {
    cptCode: "95826",
    shortDesc: "Neurology Procedure Tier 16",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 16.",
    category: "Neurology",
    workRvu: 2.55,
    facilityRvu: 7.6,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95827": {
    cptCode: "95827",
    shortDesc: "Neurology Procedure Tier 17",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 17.",
    category: "Neurology",
    workRvu: 2.6,
    facilityRvu: 7.75,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95828": {
    cptCode: "95828",
    shortDesc: "Neurology Procedure Tier 18",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 18.",
    category: "Neurology",
    workRvu: 2.65,
    facilityRvu: 7.9,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95829": {
    cptCode: "95829",
    shortDesc: "Neurology Procedure Tier 19",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 19.",
    category: "Neurology",
    workRvu: 2.7,
    facilityRvu: 8.05,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95830": {
    cptCode: "95830",
    shortDesc: "Neurology Procedure Tier 20",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 20.",
    category: "Neurology",
    workRvu: 2.75,
    facilityRvu: 8.2,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95831": {
    cptCode: "95831",
    shortDesc: "Neurology Procedure Tier 21",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 21.",
    category: "Neurology",
    workRvu: 2.8,
    facilityRvu: 8.35,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95832": {
    cptCode: "95832",
    shortDesc: "Neurology Procedure Tier 22",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 22.",
    category: "Neurology",
    workRvu: 2.85,
    facilityRvu: 8.5,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95833": {
    cptCode: "95833",
    shortDesc: "Neurology Procedure Tier 23",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 23.",
    category: "Neurology",
    workRvu: 2.9,
    facilityRvu: 8.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95834": {
    cptCode: "95834",
    shortDesc: "Neurology Procedure Tier 24",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 24.",
    category: "Neurology",
    workRvu: 2.95,
    facilityRvu: 8.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95835": {
    cptCode: "95835",
    shortDesc: "Neurology Procedure Tier 25",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 25.",
    category: "Neurology",
    workRvu: 3.0,
    facilityRvu: 8.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95836": {
    cptCode: "95836",
    shortDesc: "Neurology Procedure Tier 26",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 26.",
    category: "Neurology",
    workRvu: 3.05,
    facilityRvu: 9.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95837": {
    cptCode: "95837",
    shortDesc: "Neurology Procedure Tier 27",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 27.",
    category: "Neurology",
    workRvu: 3.1,
    facilityRvu: 9.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95838": {
    cptCode: "95838",
    shortDesc: "Neurology Procedure Tier 28",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 28.",
    category: "Neurology",
    workRvu: 3.15,
    facilityRvu: 9.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95839": {
    cptCode: "95839",
    shortDesc: "Neurology Procedure Tier 29",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 29.",
    category: "Neurology",
    workRvu: 3.2,
    facilityRvu: 9.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "95840": {
    cptCode: "95840",
    shortDesc: "Neurology Procedure Tier 30",
    longDesc: "Diagnostic and therapeutic intervention in neurology medicine, level 30.",
    category: "Neurology",
    workRvu: 3.25,
    facilityRvu: 9.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99215": {
    cptCode: "99215",
    shortDesc: "Evaluation Procedure Tier 1",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 1.",
    category: "Evaluation",
    workRvu: 1.97,
    facilityRvu: 3.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99216": {
    cptCode: "99216",
    shortDesc: "Evaluation Procedure Tier 2",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 2.",
    category: "Evaluation",
    workRvu: 2.02,
    facilityRvu: 4.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99217": {
    cptCode: "99217",
    shortDesc: "Evaluation Procedure Tier 3",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 3.",
    category: "Evaluation",
    workRvu: 2.07,
    facilityRvu: 4.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99218": {
    cptCode: "99218",
    shortDesc: "Evaluation Procedure Tier 4",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 4.",
    category: "Evaluation",
    workRvu: 2.12,
    facilityRvu: 4.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99219": {
    cptCode: "99219",
    shortDesc: "Evaluation Procedure Tier 5",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 5.",
    category: "Evaluation",
    workRvu: 2.17,
    facilityRvu: 4.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99220": {
    cptCode: "99220",
    shortDesc: "Evaluation Procedure Tier 6",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 6.",
    category: "Evaluation",
    workRvu: 2.22,
    facilityRvu: 4.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99221": {
    cptCode: "99221",
    shortDesc: "Evaluation Procedure Tier 7",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 7.",
    category: "Evaluation",
    workRvu: 2.27,
    facilityRvu: 4.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99222": {
    cptCode: "99222",
    shortDesc: "Evaluation Procedure Tier 8",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 8.",
    category: "Evaluation",
    workRvu: 2.32,
    facilityRvu: 5.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99223": {
    cptCode: "99223",
    shortDesc: "Evaluation Procedure Tier 9",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 9.",
    category: "Evaluation",
    workRvu: 2.37,
    facilityRvu: 5.15,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99224": {
    cptCode: "99224",
    shortDesc: "Evaluation Procedure Tier 10",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 10.",
    category: "Evaluation",
    workRvu: 2.42,
    facilityRvu: 5.3,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99225": {
    cptCode: "99225",
    shortDesc: "Evaluation Procedure Tier 11",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 11.",
    category: "Evaluation",
    workRvu: 2.47,
    facilityRvu: 5.45,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99226": {
    cptCode: "99226",
    shortDesc: "Evaluation Procedure Tier 12",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 12.",
    category: "Evaluation",
    workRvu: 2.52,
    facilityRvu: 5.6,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99227": {
    cptCode: "99227",
    shortDesc: "Evaluation Procedure Tier 13",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 13.",
    category: "Evaluation",
    workRvu: 2.57,
    facilityRvu: 5.75,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99228": {
    cptCode: "99228",
    shortDesc: "Evaluation Procedure Tier 14",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 14.",
    category: "Evaluation",
    workRvu: 2.62,
    facilityRvu: 5.9,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99229": {
    cptCode: "99229",
    shortDesc: "Evaluation Procedure Tier 15",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 15.",
    category: "Evaluation",
    workRvu: 2.67,
    facilityRvu: 6.05,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99230": {
    cptCode: "99230",
    shortDesc: "Evaluation Procedure Tier 16",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 16.",
    category: "Evaluation",
    workRvu: 2.72,
    facilityRvu: 6.2,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99231": {
    cptCode: "99231",
    shortDesc: "Evaluation Procedure Tier 17",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 17.",
    category: "Evaluation",
    workRvu: 2.77,
    facilityRvu: 6.35,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99232": {
    cptCode: "99232",
    shortDesc: "Evaluation Procedure Tier 18",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 18.",
    category: "Evaluation",
    workRvu: 2.82,
    facilityRvu: 6.5,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99233": {
    cptCode: "99233",
    shortDesc: "Evaluation Procedure Tier 19",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 19.",
    category: "Evaluation",
    workRvu: 2.87,
    facilityRvu: 6.65,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99234": {
    cptCode: "99234",
    shortDesc: "Evaluation Procedure Tier 20",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 20.",
    category: "Evaluation",
    workRvu: 2.92,
    facilityRvu: 6.8,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99235": {
    cptCode: "99235",
    shortDesc: "Evaluation Procedure Tier 21",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 21.",
    category: "Evaluation",
    workRvu: 2.97,
    facilityRvu: 6.95,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99236": {
    cptCode: "99236",
    shortDesc: "Evaluation Procedure Tier 22",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 22.",
    category: "Evaluation",
    workRvu: 3.02,
    facilityRvu: 7.1,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99237": {
    cptCode: "99237",
    shortDesc: "Evaluation Procedure Tier 23",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 23.",
    category: "Evaluation",
    workRvu: 3.07,
    facilityRvu: 7.25,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99238": {
    cptCode: "99238",
    shortDesc: "Evaluation Procedure Tier 24",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 24.",
    category: "Evaluation",
    workRvu: 3.12,
    facilityRvu: 7.4,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99239": {
    cptCode: "99239",
    shortDesc: "Evaluation Procedure Tier 25",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 25.",
    category: "Evaluation",
    workRvu: 3.17,
    facilityRvu: 7.55,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99240": {
    cptCode: "99240",
    shortDesc: "Evaluation Procedure Tier 26",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 26.",
    category: "Evaluation",
    workRvu: 3.22,
    facilityRvu: 7.7,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99241": {
    cptCode: "99241",
    shortDesc: "Evaluation Procedure Tier 27",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 27.",
    category: "Evaluation",
    workRvu: 3.27,
    facilityRvu: 7.85,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99242": {
    cptCode: "99242",
    shortDesc: "Evaluation Procedure Tier 28",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 28.",
    category: "Evaluation",
    workRvu: 3.32,
    facilityRvu: 8.0,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99243": {
    cptCode: "99243",
    shortDesc: "Evaluation Procedure Tier 29",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 29.",
    category: "Evaluation",
    workRvu: 3.37,
    facilityRvu: 8.15,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
  "99244": {
    cptCode: "99244",
    shortDesc: "Evaluation Procedure Tier 30",
    longDesc: "Diagnostic and therapeutic intervention in evaluation medicine, level 30.",
    category: "Evaluation",
    workRvu: 3.42,
    facilityRvu: 8.3,
    prerequisites: ["Standard Clinical Indications", "Informed Consent"]
  },
};
