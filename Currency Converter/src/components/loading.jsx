import React from 'react'

export default function loading() {
    return (
        <div>
            <div className="spinner-border text-success" role="status">
                <span className="visually-hidden">Loading...</span>
            </div>
        </div>
    )
}
