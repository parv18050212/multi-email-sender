async function sendMails() {
  const recipients = document.getElementById("recipients").value.split(",");
  const subject = document.getElementById("subject").value;
  const content = document.getElementById("content").value;

  const res = await fetch("/send-mails", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ recipients, subject, content }),
  });

  const data = await res.json();
  document.getElementById("response").innerText = data.message;
}
