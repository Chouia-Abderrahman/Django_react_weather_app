import React, { useState } from 'react';
import axios from 'axios';
import { Container, Typography, Box } from '@mui/material';
import SearchBar from './components/SearchBar';
import ItemList from './components/ItemList';

const App = () => {
    const [items, setItems] = useState([]);

    const handleSearch = async (query) => {
        try {
            const response = await axios.get(`http://localhost:8000/api/current/${query}/`);
            setItems(response.data);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <Container sx={{ mt: 4 }}>
            <Typography variant="h4" gutterBottom>
                Search List App
            </Typography>
            <SearchBar onSearch={handleSearch} />
            <Box sx={{ mt: 2 }}>
                <ItemList items={items} />
            </Box>
        </Container>
    );
};

export default App;
