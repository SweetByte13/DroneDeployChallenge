import React, { useState, useEffect } from "react";
import Card from 'react-bootstrap/Card';

function Cards({image}) {


    const image = {
        image_id,
        timestamp,
        latitude,
        longitude,
        altitude_m,
        heading_deg,
        file_name,
        camera_tilt_deg,
        focal_length_mm,
        iso,
        shutter_speed,
        aperture,
        color_temp_k,
        image_format,
        file_size_mb,
        drone_speed_mps,
        battery_level_pct,
        gps_accuracy_m,
        gimbal_mode,
        subject_detection,
        image_tags
    }

    return (
        <Card style={{ width: '18rem'}} className="cards">
            <Card.Img variant="top" src={image} className="images" />
            <Card.Body>
                <Card.Title>{image_id}</Card.Title>
                <Card.Body>{image}</Card.Body>
            </Card.Body>
        </Card>
    );
}
export default Cards;