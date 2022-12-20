from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField


app = Flask(__name__)

# Set a secret key to enable CSRF protection
app.config["SECRET_KEY"] = "your-secret-key"

# Create a form for inputting the desired duration of the yoga routine
class YogaForm(FlaskForm):
  duration = IntegerField("Duration (minutes)")
  submit = SubmitField("Create Routine")


import random

def create_yoga_routine(duration):
  # Create a dictionary to hold the yoga poses
  yoga_poses = {
    "Opening": ['Mountain Pose (Tadasana)' , "Child's Pose (Balasana)", 'Upward Salute (Urdhva Hastasana)' , 'Downward Facing Dog (Adho Mukha Svanasana)' , 'Easy Pose (Sukhasana)' , 'Cat/Cow Pose (Marjaryasana/Bitilasana)' , 'Sun Salutation (Surya Namaskar)' , 'Forward Bend (Uttanasana)'],
    "Warm Up": ["Cat/Cow Pose (Marjaryasana/Bitilasana)", "Sun Salutation (Surya Namaskar)" , "Warrior I (Virabhadrasana I)", "Warrior II (Virabhadrasana II)", "Downward Facing Dog (Adho Mukha Svanasana)" ,"Triangle Pose (Trikonasana)", "Side Angle Pose (Parsvakonasana)", "Wide-Legged Forward Bend (Prasarita Padottanasana)", "High Lunge (Anjaneyasana)", "Low Lunge (Anjaneyasana)","Plank Pose (Phalakasana)"],
    "Standing Poses": [
  "Warrior I (Virabhadrasana I)",
  "Warrior II (Virabhadrasana II)",
  "Triangle Pose (Trikonasana)",
  "Side Angle Pose (Parsvakonasana)",
  "Mountain Pose (Tadasana)",
  "Tree Pose (Vrikshasana)",
  "Eagle Pose (Garudasana)",
  "Warrior III (Virabhadrasana III)",
  "Half Moon Pose (Ardha Chandrasana)",
  "Extended Triangle Pose (Utthita Trikonasana)",
  "Lizard Pose (Utthan Pristhasana)",
  "Camel Pose (Ustrasana)",
  "Pigeon Pose (Eka Pada Rajakapotasana)"
],
    "Peak Poses": [
  "Crow Pose (Bakasana)",
  "Handstand (Adho Mukha Vrikshasana)",
  "Headstand (Sirsasana)",
  "Pincha Mayurasana (Forearm Stand)",
  "Scorpion Pose (Vrschikasana)",
  "King Pigeon Pose (Eka Pada Rajakapotasana)",
  "Dancer's Pose (Natarajasana)",
  "Wheel Pose (Urdhva Dhanurasana)",
  "Side Plank (Vasisthasana)",
  "One-Legged King Pigeon Pose (Eka Pada Rajakapotasana)",
  "King Dancer's Pose (Natarajasana)",
  "Fish Pose (Matsyasana)",
  "Shoulder Stand (Sarvangasana)"],
    "Floor Poses": [
  "Seated Forward Bend (Paschimottanasana)",
  "Pigeon Pose (Eka Pada Rajakapotasana)",
  "Cow Face Pose (Gomukhasana)",
  "Easy Seat/Cross-Legged (Sukhasana)",
  "Lizard Pose (Utthan Pristhasana)",
  "Sphinx Pose (Salamba Bhujangasana)",
  "Upward Facing Dog (Urdhva Mukha Svanasana)",
  "Fish Pose (Matsyasana)",
  "Child's Pose (Balasana)",
  "Crocodile Pose (Makarasana)",
  "Hero Pose (Virasana)",
  "Downward Facing Dog (Adho Mukha Svanasana)",
  "Bound Angle Pose (Baddha Konasana)"
],
    "Cool Down": ["Bridge Pose (Setu Bandha Sarvangasana)",
  "Shoulder Stand (Sarvangasana)",
  "Plow Pose (Halasana)",
  "Fish Pose (Matsyasana)",
  "Seated Forward Bend (Paschimottanasana)",
  "Bound Angle Pose (Baddha Konasana)",
  "Child's Pose (Balasana)",
  "Corpse Pose (Savasana)",
  "Happy Baby (Ananda Balasana)",
  "Legs Up the Wall (Viparita Karani)"],
    "Final Relaxation": [
  "Corpse Pose (Savasana)",
  "Happy Baby (Ananda Balasana)",
  "Child's Pose (Balasana)",
  "Reclined Bound Angle Pose (Supta Baddha Konasana)",
  "Legs Up the Wall (Viparita Karani)",
  "Sphinx Pose (Salamba Bhujangasana)",
  "Puppy Pose (Uttana Shishosana)",
  "Reclining Hero Pose (Supta Virasana)",
  "Reclining Goddess Pose (Supta Baddha Konasana)",
  "Reclining Big Toe Pose (Supta Padangusthasana)"
]
  }

  # Create the yoga routine as a list of tuples, with each tuple containing the category, pose, and duration
  yoga_routine = []
  for category, poses in yoga_poses.items():
    # Select a random subset of poses for each category
    if category in ["Opening","Warm Up","Cool Down","Final Relaxation"]:
      selected_poses = random.sample(poses, 2)
    elif category in ["Standing Poses", "Peak Poses", "Floor Poses"]:
      selected_poses = random.sample(poses, 3)
    else:
      selected_poses = poses

    # Calculate the duration for each pose
    for pose in selected_poses:
      pose_duration = duration // len(selected_poses)
      yoga_routine.append((category, pose, pose_duration//6))

  # Return the completed yoga routine
  return yoga_routine

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
  form = YogaForm()
  if form.validate_on_submit():
    duration = form.duration.data
    yoga_routine = create_yoga_routine(duration)
    return render_template('home.html', form=form, yoga_routine=yoga_routine)
  return render_template('home.html', form=form)



if __name__ == "__main__":


  app.run()
