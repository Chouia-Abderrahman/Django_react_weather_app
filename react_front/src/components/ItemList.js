import React from 'react';

const ItemList = ({ items }) => {
    return (
        <ul>
            {items.map((item) => (
                <li key={item.id}>{item.date_time}</li>
            ))}
        </ul>
    );
};

export default ItemList;
