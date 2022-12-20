function startRoutine() {
    // Hide the begin button
    $("#begin-button").hide();
  
    // Get the yoga routine elements
    var poses = $(".pose");
  
    // Set the current pose index to 0
    var currentPose = 0;
  
    // Start the routine
    showPose();
  
    function showPose() {
      // Get the current pose element
      var pose = poses[currentPose];
  
      // Get the duration of the pose
      var duration = parseInt($(pose).find("p:last-child").text().split(" ")[2]) * 1000;
  
     
  