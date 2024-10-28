const { exec } = require("child_process");
const path = require("path");

const processRequest = (req, res) => {
  const { singer, num_songs, clip_duration, email_id } = req.body;

  // Define the full path to main.py script
  const scriptPath = path.join(__dirname, "../../main.py");

  // Pass all necessary arguments to the main script
  const command = `python ${scriptPath} "${singer}" ${num_songs} --clip-duration ${clip_duration} --output-file final_output.mp3 "${email_id}"`;

  exec(command, (error, stdout, stderr) => {
    if (error || stderr) {
      console.error(`Error occurred: ${error.message}`);
      return res.status(500).json({ message: `Error: ${stderr || error.message}` });
    }

    // Instead of sending back all stdout, send a simpler message
    const successMessage = "The mashup process has been completed successfully.";
    res.status(200).json({ message: successMessage });
  });

};

module.exports = { processRequest };
