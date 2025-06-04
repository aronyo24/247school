import { useEffect, useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Mail, Linkedin, Github } from "lucide-react";
import { fetchTeam } from "@/services/api";

interface TeamMember {
  id: number;
  name: string;
  position: string;
  bio: string;
  photo: string;
  email: string;
  github?: string;
  linkedin?: string;
  facebook?: string;
  website?: string;
  location?: string;
}

const Teams = () => {
  const [teamMembers, setTeamMembers] = useState<TeamMember[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchTeam()
      .then((data) => {
        setTeamMembers(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching team:", err);
        setError("Failed to load team members.");
        setLoading(false);
      });
  }, []);

  return (
    <div className="min-h-screen bg-gradient-to-b from-white to-blue-50/30 py-16">
      <div className="container mx-auto px-4">
        <div className="text-center mb-16">
          <h1 className="text-4xl lg:text-6xl font-bold text-gray-800 mb-6 animate-fade-in">
            Meet Our{" "}
            <span className="bg-gradient-to-r from-eduplay-purple to-eduplay-blue bg-clip-text text-transparent">
              Amazing Team
            </span>
          </h1>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto animate-fade-in delay-150">
            Passionate educators, developers, and designers working together to
            make learning fun and accessible for every child.
          </p>
        </div>

        {loading ? (
          <p className="text-center text-gray-500">Loading team members...</p>
        ) : error ? (
          <p className="text-center text-red-500">{error}</p>
        ) : (
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
            {teamMembers.map((member, index) => (
              <Card
                key={member.id}
                className="bg-white border-0 playful-shadow hover:scale-105 transition-all duration-300 animate-fade-in"
                style={{ animationDelay: `${index * 150}ms` }}
              >
                <CardHeader className="text-center pb-4">
                  <div className="w-32 h-32 mx-auto mb-4 rounded-full overflow-hidden ring-4 ring-eduplay-purple/20">
                    <img
                      src={member.photo}
                      alt={member.name}
                      className="w-full h-full object-cover"
                    />
                  </div>
                  <CardTitle className="text-2xl font-bold text-gray-800 mb-2">
                    {member.name}
                  </CardTitle>
                  <p className="text-lg text-eduplay-purple font-semibold mb-3">
                    {member.position}
                  </p>
                </CardHeader>

                <CardContent>
                  <p className="text-gray-600 text-center mb-6 leading-relaxed">
                    {member.bio}
                  </p>
                  <div className="flex justify-center space-x-4">
                    {member.email && (
                      <a
                        href={`mailto:${member.email}`}
                        className="p-2 rounded-full bg-eduplay-blue/10 hover:bg-eduplay-blue/20 transition-colors"
                        title="Email"
                      >
                        <Mail className="w-5 h-5 text-eduplay-blue" />
                      </a>
                    )}
                    {member.linkedin && (
                      <a
                        href={`https://linkedin.com/in/${member.linkedin}`}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="p-2 rounded-full bg-eduplay-purple/10 hover:bg-eduplay-purple/20 transition-colors"
                        title="LinkedIn"
                      >
                        <Linkedin className="w-5 h-5 text-eduplay-purple" />
                      </a>
                    )}
                    {member.github && (
                      <a
                        href={`https://github.com/${member.github}`}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="p-2 rounded-full bg-gray-600/10 hover:bg-gray-600/20 transition-colors"
                        title="GitHub"
                      >
                        <Github className="w-5 h-5 text-gray-600" />
                      </a>
                    )}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        )}

        <div className="text-center mt-16">
          <div className="bg-gradient-to-r from-eduplay-purple via-eduplay-blue to-eduplay-green p-8 rounded-2xl max-w-4xl mx-auto">
            <h2 className="text-3xl font-bold text-white mb-4">Join Our Mission</h2>
            <p className="text-white/90 text-lg mb-6">
              We're always looking for passionate individuals who want to make a
              difference in education.
            </p>
            <button className="bg-white text-eduplay-purple px-8 py-3 rounded-full font-semibold hover:scale-105 transition-all duration-300">
              View Open Positions
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Teams;
