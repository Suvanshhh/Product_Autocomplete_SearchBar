import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

const Autocomplete = () => {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [loading, setLoading] = useState(false);
  const debounceTimeout = useRef(null);

  useEffect(() => {
    if (query.length < 2) {
      setSuggestions([]);
      return;
    }

    if (debounceTimeout.current) {
      clearTimeout(debounceTimeout.current);
    }

    debounceTimeout.current = setTimeout(() => {
      fetchSuggestions();
    }, 500);
  }, [query]);

  const fetchSuggestions = async () => {
    try {
      setLoading(true);
      const res = await axios.get(
        `http://localhost:8000/products/search?q=${query}&limit=10&skip=0`
      );
      setSuggestions(res.data);
    } catch (error) {
      console.error("Error fetching suggestions:", error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="autocomplete">
      <input
        type="text"
        placeholder="Search for products..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      {loading && <div className="loading">Loading...</div>}
      {!loading && suggestions.length > 0 && (
        <ul className="dropdown">
          {suggestions.map((item) => (
            <li key={item.id}>
              <strong>{item.title}</strong> ({item.brand})
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Autocomplete;
