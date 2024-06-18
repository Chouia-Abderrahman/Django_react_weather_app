import React, { useState } from 'react';
import { TextField, Button, Box } from '@mui/material';

const SearchBar = ({ onSearch }) => {
    const [query, setQuery] = useState('');

    const handleSearch = (e) => {
        e.preventDefault();
        onSearch(query);
    };

    return (
        <Box
            component="form"
            onSubmit={handleSearch}
            sx={{ display: 'flex', alignItems: 'center', mb: 2 }}
        >
            <TextField
                label="Search"
                variant="outlined"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                sx={{ marginRight: '8px' }}
                fullWidth
            />
            <Button type="submit" variant="contained" color="primary">
                Search
            </Button>
        </Box>
    );
};

export default SearchBar;
