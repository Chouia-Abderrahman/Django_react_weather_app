import React from 'react';
import { List, ListItem, ListItemText, Typography, Box, Divider } from '@mui/material';

const ItemList = ({ items }) => {
    return (
        <List>
            {items.map((item) => (
                <React.Fragment key={item.id}>
                    <ListItem alignItems="flex-start">
                        <Box>
                            <Typography variant="body1"><strong>Date/Time:</strong> {new Date(item.date_time).toLocaleString()}</Typography>
                            <Typography variant="body1"><strong>Temperature (2m):</strong> {item.temperature_2m}°C</Typography>
                            <Typography variant="body1"><strong>Relative Humidity (2m):</strong> {item.relative_humidity_2m}%</Typography>
                            <Typography variant="body1"><strong>Dew Point (2m):</strong> {item.dew_point_2m.toFixed(2)}°C</Typography>
                            <Typography variant="body1"><strong>Apparent Temperature:</strong> {item.apparent_temperature.toFixed(2)}°C</Typography>
                            <Typography variant="body1"><strong>Precipitation:</strong> {item.precipitation} mm</Typography>
                            <Typography variant="body1"><strong>Rain:</strong> {item.rain} mm</Typography>
                            <Typography variant="body1"><strong>Location Name:</strong> {item.location_name}</Typography>
                        </Box>
                    </ListItem>
                    <Divider component="li" />
                </React.Fragment>
            ))}
        </List>
    );
};

export default ItemList;
