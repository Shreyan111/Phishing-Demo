# Cybersecurity Awareness Simulator

A controlled cybersecurity awareness demonstration designed to show students how common social-engineering attacks can guide a victim from an initial message or interaction to a potentially dangerous action.

The demonstration runs entirely inside a controlled Kali Linux + Ubuntu virtual-machine environment using the same local Flask server.

---
## User Flow

1. **Start the Flask Server**
   - Run the Flask server on Kali Linux.

2. **Open the Demo**
   - From Ubuntu, open `http://<KALI-IP>:8080`.

3. **Phishing**
   - Open the simulated phishing email(html page).
   - Click the suspicious link.
   - Enter dummy credentials.
   - View the educational warning.

4. **Malicious Download**
   - Open the download demonstration.
   - Click the suspicious download.
   - Execute the harmless demo script if required.
   - Explain the risks of unknown downloads.

The above cases are for simulating malicious downloads and phishing only.
- Explain how attackers use **trust, urgency, fear, curiosity, and deception** to influence victims and execute other attacks such as Smishing, Vishing etc along with Phishing.