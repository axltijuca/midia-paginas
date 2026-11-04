# Prompts das fotos de capa/notícia (FLUX.1-Krea-dev, 1024x1280).
# Regra: nunca retratar pessoa real identificável; marcas e rótulos genéricos; estilo fotojornalismo.
STYLE = ", candid documentary sports photography, shot on Sony A7 IV 35mm f/1.8, natural skin texture, film grain, no text, no logos"
LAB = ", dark gritty gym, low-key lighting with warm red rim light"
RADAR = ", industrial arena, cool lighting with neon lime green accents"

PROMPTS = {
 "lab": {
  "01": "Close-up of a lifter's chalked hands tightening a leather lifting belt next to a shaker bottle and a cup of black coffee on a gym bench" + LAB,
  "02": "Muscular man scooping white powder from a plain unbranded tub into a shaker, chalk dust in the air" + LAB,
  "03": "Olympic-style swimming pool at night seen from the stands, empty lanes, dramatic arena lights and reflections, Las Vegas atmosphere",
  "04": "Athlete drinking espresso from a small cup in a gym before training, steam rising, barbell blurred in background" + LAB,
  "05": "Medical vials and a syringe on a stainless steel tray beside blood test paperwork, clinical cold light with a red accent, no labels",
  "07": "Nurse drawing blood from the arm of a muscular athlete in a clinic, test tubes in a rack, soft clinical light",
  "08": "Anti-doping control room: sealed urine sample kit boxes and tamper-proof bottles on a table, official badge lanyard, neutral light",
  "09": "Small glass peptide vials and a lab pipette on a dark laboratory bench, scientific glassware, moody red rim light, no labels",
  "10": "Bodybuilder posing on a competition stage under bright spotlights, deep tan, dark background with golden stage glow, seen from behind the judges, face not visible",
  "11": "Heavy barbell squat in a power rack, athlete at the bottom of the rep, plates loaded, intense moment" + LAB,
  "12": "Coach with a clipboard watching a bodybuilder train on a cable machine, focused discussion" + LAB,
  "14": "Coach correcting a lifter's deadlift technique, hand pointing at hip position, educational moment" + LAB,
  "15": "University sports science lab with a lifter on a force plate, laptop showing graphs, students observing, professional lighting with red accent",
 },
 "radar": {
  "01": "Hybrid fitness race inside a huge exhibition hall, athletes pushing heavy sleds on a turf lane, crowd and lights in background" + RADAR,
  "02": "Massive indoor fitness race venue being set up, rows of rowing machines and ski ergs, banners without text, wide shot" + RADAR,
  "03": "Split scene: athlete doing barbell clean in a functional training box and another running on an indoor track, gritty texture" + RADAR,
  "04": "Functional fitness competition in a stadium, athlete lifting a barbell overhead, crowd cheering, stage lights" + RADAR,
  "05": "Exhausted first-time racer on hands and knees after wall balls in an indoor race, sweat, determination" + RADAR,
  "06": "Athlete in a gym doing kettlebell swings with an assault bike and barbell nearby, sweat and motion blur" + RADAR,
  "07": "Runner crossing the finish line of an indoor fitness race with arms raised, confetti, blurred crowd" + RADAR,
  "08": "Packed modern gym in Brazil at night, many people training, wide-angle view of rows of machines" + RADAR,
  "09": "Coach with a stopwatch shouting encouragement to an athlete on a rowing machine during intervals" + RADAR,
  "11": "Fitness professionals at work: physiotherapist assessing a knee, coach programming on a tablet, gym setting" + RADAR,
  "12": "Young students in a sports science classroom with exercise physiology charts, one holding a kettlebell, bright lighting" + RADAR,
  "13": "Fitness merchandise pop-up store inside an event hall, shelves with plain unbranded shoes and apparel, warm retail lighting" + RADAR,
  "14": "Elite performance coach analyzing data on a laptop beside a track while an athlete sprints in the background" + RADAR,
  "15": "Strength athlete chalking hands before a heavy lift, university sports lab in background, professional lighting" + RADAR,
 },
}
PROMPTS = {pg: {k: v + STYLE for k, v in d.items()} for pg, d in PROMPTS.items()}
