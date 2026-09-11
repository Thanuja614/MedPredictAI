/**
 * MedPredict AI — Medical Clinical Timeline Component
 * Clean, vertical chronological timeline with connected circular nodes
 */

import React from 'react';
import { Activity, FileText, FlaskConical, Pill, Stethoscope, Calendar } from 'lucide-react';

export interface TimelineEvent {
  id: string;
  date: string;
  year: string;
  title: string;
  category: 'prediction' | 'lab' | 'encounter' | 'medication';
  description: string;
  provider?: string;
  badge?: string;
}

interface MedicalTimelineProps {
  events: TimelineEvent[];
}

export const MedicalTimeline: React.FC<MedicalTimelineProps> = ({ events }) => {
  const getEventIcon = (category: TimelineEvent['category']) => {
    switch (category) {
      case 'prediction':
        return <Activity className="w-3.5 h-3.5 text-medblue" />;
      case 'lab':
        return <FlaskConical className="w-3.5 h-3.5 text-teal" />;
      case 'medication':
        return <Pill className="w-3.5 h-3.5 text-sage" />;
      case 'encounter':
        return <Stethoscope className="w-3.5 h-3.5 text-navy-800" />;
      default:
        return <FileText className="w-3.5 h-3.5 text-slateText" />;
    }
  };

  return (
    <div className="bg-surface rounded-card p-6 border border-borderLine shadow-medical space-y-4">
      <div className="flex items-center justify-between border-b border-borderLine pb-3">
        <div>
          <h3 className="font-serif text-lg font-bold text-navy-800">
            Longitudinal Clinical Timeline
          </h3>
          <p className="text-xs text-slateText">
            Chronological log of clinical encounters, diagnostic evaluations, and pharmacological changes
          </p>
        </div>
        <span className="text-xs font-semibold text-slateText px-2 py-1 bg-ivory rounded border border-borderLine">
          {events.length} Recorded Events
        </span>
      </div>

      <div className="relative pl-6 space-y-6 before:content-[''] before:absolute before:left-[11px] before:top-3 before:bottom-3 before:w-0.5 before:bg-borderLine">
        {events.map((evt) => (
          <div key={evt.id} className="relative group">
            {/* Circular Marker Node */}
            <div className="absolute -left-[23px] top-1.5 w-6 h-6 rounded-full bg-surface border-2 border-borderLine flex items-center justify-center shadow-xs group-hover:border-medblue transition">
              {getEventIcon(evt.category)}
            </div>

            {/* Event Content Box */}
            <div className="bg-ivory/70 hover:bg-ivory p-3.5 rounded-btn border border-borderLine transition-all">
              <div className="flex items-center justify-between flex-wrap gap-1">
                <div className="flex items-center space-x-2">
                  <span className="text-xs font-bold text-navy-800">{evt.title}</span>
                  {evt.badge && (
                    <span className="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-medblue-light text-medblue border border-medblue/20">
                      {evt.badge}
                    </span>
                  )}
                </div>
                <div className="flex items-center space-x-1 text-[11px] text-slateText font-mono">
                  <Calendar className="w-3 h-3" />
                  <span>{evt.date}</span>
                </div>
              </div>

              <p className="text-xs text-slate-700 mt-1.5 leading-relaxed">
                {evt.description}
              </p>

              {evt.provider && (
                <div className="mt-2 text-[10px] text-slateText flex items-center space-x-1 border-t border-borderLine/50 pt-1.5">
                  <span className="font-semibold text-charcoal">Clinician:</span>
                  <span>{evt.provider}</span>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
