## Quantitative Assessment Report

Method: Simulated 100 / 500 /1000 requests/second for 1 minute

Test Tool: Locust  

## Test Summary
The system is reliable at 100–500 requests per second with a failure rate below 1%. However, at 1,000 requests per second, the failure rate increases to 6%, indicating a bottleneck

| Request Rate (requests/s) | Avg Response Time (ms) | 95th % Response Time (ms) | Max Response Time (ms) | Failure Rate (%) | Achieved Requests/s |
|---------------------------|-------------------------|---------------------------|------------------------|------------------|---------------------|
| 100                       | 22.87                  | 64                        | 310.57                 | 0.0%             | 34.11              |
| 500                       | 57.84                  | 180                       | 1,435.92               | 0.4%             | 168.20             |
| 1,000                     | 290.78                 | 1,700                     | 2,686.01               | 6.8%             | 308.68             |


## Appendix

[1] Simulated 100 requests/second for 1 minute : failure rate is 0.0%
| Type     | Name        | Request Count | Failure Count | Median Response Time (ms) | Average Response Time (ms) | Min Response Time (ms) | Max Response Time (ms) | Average Content Size (bytes) | Requests/s | Failures/s | 50% (ms) | 66% (ms) | 75% (ms) | 80% (ms) | 90% (ms) | 95% (ms) | 98% (ms) | 99% (ms) | 99.9% (ms) | 99.99% (ms) | 100% (ms) |
|----------|-------------|---------------|---------------|---------------------------|----------------------------|-------------------------|-------------------------|------------------------------|------------|------------|----------|----------|----------|----------|----------|----------|----------|----------|------------|-------------|-----------|
| GET      | /           | 2,015         | 0             | 10                        | 22.87                     | 8.94                   | 310.57                 | 862.0                       | 34.11      | 0.0        | 10       | 11       | 16       | 32       | 35       | 64       | 180      | 230      | 310        | 310         | 310       |
|          | Aggregated  | 2,015         | 0             | 10                        | 22.87                     | 8.94                   | 310.57                 | 862.0                       | 34.11      | 0.0        | 10       | 11       | 16       | 32       | 35       | 64       | 180      | 230      | 310        | 310         | 310       |


[2] Simulated 500 requests/second for 1 minute : failure rate is 0.4%
| Type     | Name        | Request Count | Failure Count | Median Response Time (ms) | Average Response Time (ms) | Min Response Time (ms) | Max Response Time (ms) | Average Content Size (bytes) | Requests/s | Failures/s | 50% (ms) | 66% (ms) | 75% (ms) | 80% (ms) | 90% (ms) | 95% (ms) | 98% (ms) | 99% (ms) | 99.9% (ms) | 99.99% (ms) | 100% (ms) |
|----------|-------------|---------------|---------------|---------------------------|----------------------------|-------------------------|-------------------------|------------------------------|------------|------------|----------|----------|----------|----------|----------|----------|----------|----------|------------|-------------|-----------|
| GET      | /           | 9,941         | 40            | 11                        | 57.84                     | 8.60                   | 1,435.92                | 858.67                      | 168.20     | 0.68       | 11       | 13       | 31       | 33       | 36       | 180      | 950      | 1,200    | 1,400      | 1,400       | 1,400     |
|          | Aggregated  | 9,941         | 40            | 11                        | 57.84                     | 8.60                   | 1,435.92                | 858.67                      | 168.20     | 0.68       | 11       | 13       | 31       | 33       | 36       | 180      | 950      | 1,200    | 1,400      | 1,400       | 1,400     |


[3] Simulated 1000 requests/second for 1 minute : failure rate is 6.8%
| Type     | Name        | Request Count | Failure Count | Median Response Time (ms) | Average Response Time (ms) | Min Response Time (ms) | Max Response Time (ms) | Average Content Size (bytes) | Requests/s | Failures/s | 50% (ms) | 66% (ms) | 75% (ms) | 80% (ms) | 90% (ms) | 95% (ms) | 98% (ms) | 99% (ms) | 99.9% (ms) | 99.99% (ms) | 100% (ms) |
|----------|-------------|---------------|---------------|---------------------------|----------------------------|-------------------------|-------------------------|------------------------------|------------|------------|----------|----------|----------|----------|----------|----------|----------|----------|------------|-------------|-----------|
| GET      | /           | 18,270        | 1,199         | 61                        | 290.78                    | 8.68                   | 2,686.01                | 807.66                      | 308.68     | 20.26      | 61       | 100      | 160      | 600      | 1,100    | 1,200    | 1,700    | 2,100    | 2,400      | 2,400       | 2,700     |
|          | Aggregated  | 18,270        | 1,199         | 61                        | 290.78                    | 8.68                   | 2,686.01                | 807.66                      | 308.68     | 20.26      | 61       | 100      | 160      | 600      | 1,100    | 1,200    | 1,700    | 2,100    | 2,400      | 2,400       | 2,700     |



