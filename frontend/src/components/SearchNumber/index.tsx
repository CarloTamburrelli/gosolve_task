import { useState } from 'react'
import './SearchNumber.css';
import { API_URL } from '../../constants';

function SearchNumber() {
  const [number, setNumber] = useState<number | null>(null);

  const [result, setResult] = useState<string>('');

  const [loading, setLoading] = useState<boolean>(false)
  const [error, setError] = useState<string>('')

  const handleSearch = async () => {
    if (number === null || number === undefined) return

    setLoading(true)
    setError('')
    setResult('')

    try {
      const response = await fetch(`${API_URL}/endpoint/${number}`);
    
      if (!response.ok) {
        // index not found or internal error
        const errorData = await response.json();
        setError(errorData.error || 'Unknown error from server');
        setResult('');
      } else {
        const data = await response.json();
        if (data.index !== undefined && data.index !== null) {
          setResult(`Index found: ${data.index}`);
          setError('');
        } else {
          setError('Invalid server response');
          setResult('');
        }
      }
    } catch (err) {
      setError('Error during request');
      setResult('');
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="search-wrapper">
      <div className="search-row">
        <input
          type="number"
          placeholder="Enter a number"
          value={number !== null && number !== undefined ? number : ''}
          onChange={(e) => {
            const val = e.target.value;
            setNumber(val === '' ? null : Number(val));
          }}
          className="search-input"
        />
        <button
          onClick={handleSearch}
          disabled={loading}
          className="search-button"
        >
          {loading ? 'Loading...' : 'Search'}
        </button>
      </div>

      <div className="search-result">
        {error && <div className="search-error">{error}</div>}
        {result && <div className="search-response">{result}</div>}
      </div>
    </div>
  )
}

export default SearchNumber
