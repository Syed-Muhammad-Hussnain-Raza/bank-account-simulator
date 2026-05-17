let balance = 0;

function getAmount() {
  return parseFloat(document.getElementById("amount").value);
}

function setMessage(text, type) {
  const msg = document.getElementById("message");
  msg.textContent = text;
  msg.className = "message " + type;
}

function updateBalance() {
  document.getElementById("balance").textContent = "$" + balance.toFixed(2);
}

function addToHistory(type, amount) {
  const body = document.getElementById("history-body");
  const emptyRow = document.getElementById("empty-row");
  if (emptyRow) emptyRow.remove();

  const now = new Date();
  const time = now.toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
  });

  const row = document.createElement("tr");
  row.innerHTML = `
    <td class="${type}-type">${type === "deposit" ? "↑ Deposit" : "↓ Withdraw"}</td>
    <td>$${amount.toFixed(2)}</td>
    <td>$${balance.toFixed(2)}</td>
    <td>${time}</td>
  `;
  body.prepend(row);
}

function deposit() {
  const amount = getAmount();

  if (isNaN(amount) || document.getElementById("amount").value === "") {
    setMessage("Please enter a valid amount.", "error");
    return;
  }
  if (amount <= 0) {
    setMessage("Amount must be positive.", "error");
    return;
  }

  balance += amount;
  updateBalance();
  addToHistory("deposit", amount);
  setMessage(`$${amount.toFixed(2)} deposited successfully.`, "success");
  document.getElementById("amount").value = "";
}

function withdraw() {
  const amount = getAmount();

  if (isNaN(amount) || document.getElementById("amount").value === "") {
    setMessage("Please enter a valid amount.", "error");
    return;
  }
  if (amount <= 0) {
    setMessage("Amount must be positive.", "error");
    return;
  }
  if (amount > balance) {
    setMessage("Insufficient funds. Overdraft not allowed.", "error");
    return;
  }

  balance -= amount;
  updateBalance();
  addToHistory("withdraw", amount);
  setMessage(`$${amount.toFixed(2)} withdrawn successfully.`, "success");
  document.getElementById("amount").value = "";
}

function resetAccount() {
  balance = 0;
  updateBalance();
  setMessage("Account has been reset.", "success");
  document.getElementById("amount").value = "";

  const body = document.getElementById("history-body");
  body.innerHTML = `
    <tr id="empty-row">
      <td colspan="4" class="empty">No transactions yet.</td>
    </tr>
  `;
}
