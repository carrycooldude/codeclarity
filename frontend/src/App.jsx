import React, { useState } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';

function App() {
  const [results, setResults] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    setLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:8000/analyze', formData);
      setResults(response.data);
    } catch (error) {
      console.error('Analysis failed:', error);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: '20px', maxWidth: '800px', margin: '0 auto' }}>
      <h1>CodeClarity</h1>
      <input type="file" onChange={handleFileUpload} accept=".py,.js,.java" />
      
      {loading && <p>Analyzing code...</p>}
      
      {results && (
        <div>
          <h2>Code Summary</h2>
          <p>{results.summary}</p>
          
          <h2>Generated Documentation</h2>
          <ReactMarkdown>{results.documentation}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}

export default App;