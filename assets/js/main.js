import htm from "https://dev.jspm.io/htm@3.1.1";
import React, { useState, useEffect } from "https://dev.jspm.io/react@18.2.0";
import ReactDOM from "https://dev.jspm.io/react-dom@18.2.0";

const html = htm.bind(React.createElement);

async function fetchAliasesData() {
  try {
    const response = await fetch("assets/data/aliases.json");

    if (!response.ok) {
      throw new Error("Failed to fetch data");
    }

    return await response.json();
  } catch (error) {
    console.error("Error fetching data:", error);
    return [];
  }
}

function App() {
  const [aliases, setAliases] = useState([]);
  const [searchQuery, setSearchQuery] = useState("");

  useEffect(() => {
    async function fetchData() {
      const data = await fetchAliasesData();
      setAliases(data);
    }
    fetchData();
  }, []);

  // Filter aliases based on search query
  const filteredAliases = aliases.filter(
    (alias) =>
      alias.alias.toLowerCase().includes(searchQuery.toLowerCase()) ||
      alias.definition.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return html`
    <div className="container">
      <h2>Bash Aliases</h2>
      <div>
        <label for="searchInput">Filter:</label>
        <input
          id="searchInput"
          type="text"
          placeholder="Search alias or definition..."
          value=${searchQuery}
          onChange=${(e) => setSearchQuery(e.target.value)}
        />
      </div>
      <table className="aliases-table">
        <thead>
          <tr>
            <th>Alias</th>
            <th>Definition</th>
            <th>Comment</th>
          </tr>
        </thead>
        <tbody>
          ${filteredAliases.map((alias, index) => html`
            <tr key=${index}>
              <td className="monospaced alias-column">${alias.alias}</td>
              <td className="monospaced definition-column">${alias.definition}</td>
              <td>${alias.comment}</td>
            </tr>
          `)}
        </tbody>
      </table>
    </div>
  `;
}

ReactDOM.render(html`<${App} />`, document.getElementById("app"));
