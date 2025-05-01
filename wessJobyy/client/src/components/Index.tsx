import { useEffect, useState } from "react";
import Header from "../components/Header";
import SearchBar from "../components/SearchBar";
import JobCard from "../components/JobCard";
import axios from "axios";
import { useQuery } from "@tanstack/react-query";

const Index = () => {
    const [jobListings, setJobListings] = useState<any[]>([]);
    const [Loading, setLoading] = useState(false);
    const {data, isLoading, isError} = useQuery({
        queryKey: ["jobListings"],
        queryFn: async () => {
            const res = await axios.get("http://127.0.0.1:8000/jobsList/software developer");
            return res.data;
        },
    })

    useEffect(()=>{
        if(data){
            setJobListings(data);
        }
    }, [data]);


    const handleSearch = async(query: string) => {
        if(!query) return;
        setLoading(true);
        try {
            const res = await axios.get(`http://127.0.0.1:8000/jobsList/${query}`);
            setJobListings(res.data);
        } catch (error) {
            console.error("Error fetching job listings:", error);
        } finally {
            setLoading(false);
        }
    };

    return (
    <div className="min-h-screen bg-gradient-radial from-blue-100/30 via-white to-pink-100/30">
        <div className="container px-4 py-8 mx-auto max-w-6xl">
            <Header />

            <div className="mt-8 flex justify-center">
                <SearchBar onSearch={handleSearch} />
            </div>

            <div className="mt-12 space-y-6">
                {(Loading || isLoading) && <div className="text-center text-gray-500">Loading...</div>}
                {isError && <div className="text-center text-red-500">Error fetching job listings</div>}
                {jobListings.length === 0 && !isLoading && !isError && (
                    <div className="text-center text-gray-500">No job listings found</div>
                )}
                {((!Loading && !isLoading) && jobListings.length > 0) && jobListings?.map((job:any,idx:number) => (
                    <JobCard
                        key={idx}
                        title={job.title}
                        date={job.posted}
                        company={job.company || "Unknown Company"}
                        location={job.location}
                        workType={job.work_state}
                        description={job.experience}
                        link={job.job_link}
                    />
                ))}
            </div>
        </div>
    </div>
    );
};

export default Index;
