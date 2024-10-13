const { exec } = require("child_process");
const path = require("path");

const processRequest = (req, res) => {
  const { singer, num_songs, clip_duration, email_id } = req.body;

  // Define the full path to main.py script
  const scriptPath = path.join(__dirname, "../../main.py");

  // Pass all necessary arguments to the main script
  const command = `python ${scriptPath} "${singer}" ${num_songs} --clip-duration ${clip_duration} --output-file final_output.mp3 "${email_id}"`;

  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error occurred: ${error.message}`);  
      res.status(500).json({ message: `Script execution failed: ${stderr || error.message}` });
    } 
    if (stderr) {
        console.error(`Script stderr: ${stderr}`);
        return res.status(500).json({ message: `Error: ${stderr}` });
    }

    res.status(200).json({ message: `Script output: ${stdout}` });
  });
};

module.exports = { processRequest };
