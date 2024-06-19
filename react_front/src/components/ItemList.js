import React from 'react';
import { List, ListItem, Typography, Box, Divider, Grid } from '@mui/material';

const ItemList = ({ items }) => {
    return (
        <Box sx={{ width: '100%', bgcolor: 'background.paper' }}>
            <Box sx={{ alignItems: 'center', padding: '16px' }}>
                <Grid container spacing={2}>
                    <Grid item xs={2}><Typography variant="subtitle2">date_time</Typography></Grid>
                    <Grid item xs={1}><Typography variant="subtitle2">Temperature</Typography></Grid>
                    <Grid item xs={0.7}><Typography variant="subtitle2">Humidity</Typography></Grid>
                    <Grid item xs={1}><Typography variant="subtitle2">dew_point_2m</Typography></Grid>
                    <Grid item xs={1.5}><Typography variant="subtitle2">apparent_temperature</Typography></Grid>
                    <Grid item xs={1}><Typography variant="subtitle2">Precipitation</Typography></Grid>
                    <Grid item xs={0.7}><Typography variant="subtitle2">Rain</Typography></Grid>
                    <Grid item xs={1.3}><Typography variant="subtitle2">wind_speed_10m</Typography></Grid>
                    <Grid item xs={1}><Typography variant="subtitle2">location</Typography></Grid>
                </Grid>
            </Box>
            <Divider />
            {items.map((item) => (
                <React.Fragment key={item.id}>
                    <ListItem sx={{ display: 'flex', alignItems: 'center' }}>
                        <Grid container spacing={2}>
                            <Grid item xs={2}><Typography>{new Date(item.date_time).toLocaleString()}</Typography></Grid>
                            <Grid item xs={1}><Typography>{item.temperature_2m.toFixed(2)}</Typography></Grid>
                            <Grid item xs={0.7}><Typography>{item.relative_humidity_2m}%</Typography></Grid>
                            <Grid item xs={1}><Typography>{item.dew_point_2m.toFixed(2)}</Typography></Grid>
                            <Grid item xs={1.5}><Typography>{item.apparent_temperature.toFixed(2)}</Typography></Grid>
                            <Grid item xs={1}><Typography>{item.precipitation.toFixed(2)}</Typography></Grid>
                            <Grid item xs={0.7}><Typography>{item.rain.toFixed(2)}</Typography></Grid>
                            <Grid item xs={1.3}><Typography>{item.wind_speed_10m.toFixed(2)}</Typography></Grid>
                            <Grid item xs={1}><Typography>{item.location_id.name}</Typography></Grid>
                        </Grid>
                    </ListItem>
                    <Divider />
                </React.Fragment>
            ))}
        </Box>
    );
};

export default ItemList;
