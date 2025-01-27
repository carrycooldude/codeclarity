async function generateDocs() {
    const code = document.getElementById("code").value;
    const response = await fetch("/generate_docs", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code }),
    });
    const docs = await response.json();
    document.getElementById("docs").innerText = JSON.stringify(docs, null, 2);
}