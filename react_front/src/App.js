import React, { useState } from 'react';
import axios from 'axios';
import SearchBar from './components/SearchBar';
import ItemList from './components/ItemList';

const App = () => {
    const [items, setItems] = useState([]);

    const handleSearch = async (query) => {
        try {
            console.log("fetching data")
            const response = await axios.get(`http://localhost:8000/api/current/${query}/`);
            setItems(response.data);
            console.log(response.data)
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <div>
            <h1>Search List App</h1>
            <SearchBar onSearch={handleSearch} />
            <ItemList items={items} />
        </div>
    );
};

export default App;
